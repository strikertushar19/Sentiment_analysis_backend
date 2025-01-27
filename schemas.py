from pydantic import BaseModel

class FileRequest(BaseModel):
    filename: str

class FileResponse(BaseModel):
    id: int
    filename: str