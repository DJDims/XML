from typing import List, Optional
from pydantic import BaseModel

class Category(BaseModel):  #Класс описывающий категорию
    id: Optional[int]
    name: str
    class Config:
        orm_mode = True

