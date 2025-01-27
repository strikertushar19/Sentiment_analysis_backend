import re
from fastapi import FastAPI, HTTPException, Depends, UploadFile, File
from sqlalchemy.orm import Session
import sys
import os
from fuzzywuzzy import fuzz

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from openai import OpenAI
from database.database import SessionLocal, engine, File

import openai
from dotenv import load_dotenv
from typing import List, Dict, Any
import asyncio

load_dotenv()

app = FastAPI()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def query_openai(messages: List[Dict[str, str]]):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response
    except openai.OpenAIError as e:
        raise HTTPException(status_code=500, detail=f"OpenAI API error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

def list_files(db: Session):
    files = db.query(File).all()
    if not files:
        raise HTTPException(status_code=404, detail="No files found in the database.")
    return files

async def chat_with_agent(user_input: str):
    # Define a system message to tell GPT-3.5 that it has access to the database where PDFs are stored
    system_message = {
        "role": "system",
        "content": (
            "You are a GPT-3.5 model running in local development mode. "
            "You have access to a database where PDF files are stored, "
            "and you can search for those files by filename. "
            "Please use the provided database search function to locate the relevant PDFs if needed."
            "I want you to generate just the pdf name that the user is asking for, nothing else."
            "Generate response like: pdf is pdfname."
        )
    }

    # Step 1: Construct the conversation messages
    messages = [system_message, {"role": "user", "content": user_input}]

    # Step 2: Send the user input to OpenAI API
    response = query_openai(messages)
        
    return response

def extract_and_clean_pdf_name(response_content: str):
    match = re.search(r'\S+\.pdf', response_content.strip())
    if match:
        pdf_name = match.group(0)
        cleaned_name = pdf_name.replace(" ", "").replace("_", "").lower()
        return cleaned_name
    return None

def search_closest_pdf(pdf_name: str, db: Session):
    files = db.query(File).all()
    closest_match = None
    highest_similarity = 0

    for file in files:
        db_filename = file.filename.replace(" ", "").replace("_", "").lower()
        similarity = fuzz.ratio(pdf_name, db_filename)

        if similarity > highest_similarity:
            highest_similarity = similarity
            closest_match = file

    return closest_match



from fastapi import Response

async def handle_request(user_input: str):
    obj = await chat_with_agent(user_input)
    
    response_content = obj.choices[0].message.content
    print(response_content)
    
    pdf_name = extract_and_clean_pdf_name(response_content)
    
    if not pdf_name:
        print("No PDF name found in the response.")
        return None  # Just return None if no PDF name is found
    
    print(f"Extracted PDF name: {pdf_name}")
    
    db = SessionLocal()
    
    try:
        # Search for the closest PDF in the database
        closest_pdf = search_closest_pdf(pdf_name, db)
        
        if closest_pdf:
            # Assuming closest_pdf is an instance of the File model
            return Response(
                content=closest_pdf.content,  # The binary content of the PDF
                media_type="application/pdf",
                headers={"Content-Disposition": f"attachment; filename={closest_pdf.filename}"}
            )
        else:
            print("No similar PDF found in the database.")
            return None  # Or handle as needed
    
    finally:
        db.close()

def main():
    asyncio.run(handle_request("I want computer networks pdf"))

if __name__ == "__main__":
    main()
