from pydantic import BaseModel
from fastapi import Form

class Image(BaseModel):
    height: int = Form(...)

    @classmethod
    def as_form(cls, height: int = Form(...)):
        return cls(height=height)