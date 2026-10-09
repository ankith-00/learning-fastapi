from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator
from typing import List, Dict, Optional, Annotated

app = FastAPI()


# - - - - - - - - - - - - - - - creating simple pydantic model
# class User(BaseModel):
#     id:int
#     name:str
#     email:str


# - - - - - - - - - - - - - - - creating pydantic modal using 'List' & 'Dict' from typing
class Student(BaseModel):
    roll_no: int
    name: str = Annotated[str, Field(max_length=30, title="Name should be within 50 chars")]
    active: Annotated[bool, Field(default=None, description="This represents students addmission status")]
    subjects: List[str]
    marks: Dict[str, float]
    phone_no: Optional[int] = None     # defining Optional requires 'default' 'None' 
    email: EmailStr                
    dp_image_url:AnyUrl  
    age: int = Field(gt=15, lt=25) 


    @field_validator("email")          # custome field validator using field_validator decorator
    @classmethod
    def validate_email(class_instance, email_value):
        valid_domains = ["google.com", "sarvam.com"]   
        domain_name = email_value.split("@")[-1]
        if domain_name not in valid_domains:
            raise ValueError("Invalid Email")
        return email_value


    @model_validator(mode="after")
    def validate_marks(self):
        if self.marks.get("Math", 0) < 10:
            raise ValueError("Math marks cannot be less then 10")
        return self



student_info = {"roll_no":2 ,'name': "Ravi", "active": True, "subjects":["Math", "English"], "marks": {"English": 45.6, "Math": 11}, "email":"abc@sarvam.com", "dp_image_url": "http://www.ankith.dev/image.png", "age": 16}

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