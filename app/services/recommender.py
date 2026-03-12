from sqlalchemy.orm import Session
from app.models.recipe import Recipe
from app.models.record import DietRecord
from sqlalchemy import func
import random

def get_recommendation(user_id: int, db: Session, user_level: int):
    # 简单的推荐逻辑：
    # 1. 优先获取用户最常吃的健康分高的菜谱
    # 2. 如果是高级用户，提供更详细的推荐分析
    
    # 模拟逻辑：随机推荐，后续在此扩展复杂的算法
    recipes = db.query(Recipe).all()
    if not recipes:
        return None
    
    recommendation = random.choice(recipes)
    
    # 权限校验：如果是普通用户，隐藏详细营养分析
    if user_level < 2:
        return {" name:
