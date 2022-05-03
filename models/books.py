from pydantic import BaseModel

class Books(BaseModel):
    title: str
    author:  str
    number_pages: int
    publisher: str

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}