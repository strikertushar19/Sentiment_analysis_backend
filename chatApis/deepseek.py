from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import os

# Define the relative path
save_directory = "./deepSeek-R1-Distill-Llama-8B"

# Convert to absolute path (optional, for debugging)
absolute_path = os.path.abspath(save_directory)
print("Absolute Path of Save Directory:", absolute_path)

# Load the tokenizer and model
print("Loading model and tokenizer from Hugging Face Hub...")

tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/DeepSeek-R1-Distill-Llama-8B")
model = AutoModelForCausalLM.from_pretrained("deepseek-ai/DeepSeek-R1-Distill-Llama-8B")

# Save the tokenizer and model
print(f"Saving model and tokenizer to {save_directory}...")
tokenizer.save_pretrained(save_directory)
model.save_pretrained(save_directory)

# Load the tokenizer and model from the local directory
print("Loading model and tokenizer from local directory...")
tokenizer = AutoTokenizer.from_pretrained(save_directory)
model = AutoModelForCausalLM.from_pretrained(save_directory)

print("Model and tokenizer loaded successfully!")

# Test the model with some input
test_input = "Once upon a time"

# Tokenize the input text
inputs = tokenizer(test_input, return_tensors="pt")

# Generate text using the model
outputs = model.generate(inputs['input_ids'], max_length=50, num_return_sequences=1)

# Decode the generated tokens back into text
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print("Generated Text:")
print(generated_text)
