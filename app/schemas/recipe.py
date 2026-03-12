from pydantic import BaseModel
from typing import List, Optional

class RecipeBase(BaseModel):
    name: str
    ingredients: list
    instructions: str
    calories: float
    protein: float
    fat: float
    carbs: float
    difficulty: str

class RecipeCreate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: int

    class Config:
        from_attributes = True
