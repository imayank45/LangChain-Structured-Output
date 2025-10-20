from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    
    name:str = 'mayank'
    age:Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, description='A decimal value representing the cgpa of the student')
    
new_Student = {'age':'24', 'email':'abc@gmail.com', 'cgpa':7.8}
student = Student(**new_Student)

print(student)