from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Optional

app = FastAPI()


# - - - - - - - - - - - - - - - creating simple pydantic model
# class User(BaseModel):
#     id:int
#     name:str
#     email:str


# - - - - - - - - - - - - - - - creating pydantic modal using 'List' & 'Dict' from typing
class Student(BaseModel):
    roll_no: int
    name: str
    active: bool
    subjects: List[str]
    marks: Dict[str, float]
    phone_no: Optional[int] = None       # Defining Optional requires 'default' 'None'            



student_info = {"roll_no":2 ,'name': "Ravi", "active": True, "subjects":["Math", "English"], "marks": {"English": 45.6}}

student1 = Student(**student_info)

def print_student_data(student: Student):
    print("Students details : {",student, "}")

print_student_data(student1)










# user_data = [
#     {
#         "id": 1,
#         "name": "Rajeev",
#         "age": 20,
#         "email": "rajeev@gmail.com",
#         "city": "Bengaluru"
#     }
# ]


# @app.get('/', response_model=User)
# def root():
#     return user_data[0]