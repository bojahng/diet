from sqlalchemy import Column, Integer, String, Float, JSON
from app.core.database import Base

class Recipe(Base):
    __tablename__ = 'recipes'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    ingredients = Column(JSON)  # 存储配料清单
    instructions = Column(String)  # 烹饪步骤
    calories = Column(Float)
    protein = Column(Float)
    fat = Column(Float)
    carbs = Column(Float)
    difficulty = Column(String)  # 简单/中等/困难
