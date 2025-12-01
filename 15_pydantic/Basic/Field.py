from pydantic import BaseModel , Field
from typing import List,Dict,Optional

class Employee(BaseModel):
    id:int
    name:str = Field(
        ..., #tells us that these fields are important 
        min_length=3,
        max_length=50,
        description="Enter your Name please",
        examples="Jhon Boby "
    )

    Department: Optional[str] = "general"

    Salary : float = Field(
        ..., #cumpulsory 
        ge=10000,
        le=50000,
        description="Annual salary in USD",
    )