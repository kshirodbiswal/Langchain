from pydantic  import BaseModel,EmailStr
from typing import Optional

class student(BaseModel):
    name:str = "rajaa"
    age:Optional['int'] =32
new_student={'name':"rajaa",'age':22}
student=student(**new_student)

print(student)
print(type(student))