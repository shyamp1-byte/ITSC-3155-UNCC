from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import Recipe
from schemas import RecipeCreate, RecipeUpdate

def create(db: Session, recipe: RecipeCreate):
    db_recipe = Recipe(
        sandwich_id=recipe.sandwich_id,
        resource_id=recipe.resource_id,
        amount=recipe.amount
    )
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def update(db: Session, recipe: RecipeUpdate, recipe_id: int):
    db_recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not db_recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    db_recipe.sandwich_id = recipe.sandwich_id
    db_recipe.resource_id = recipe.resource_id
    db_recipe.amount = recipe.amount
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def delete(db: Session, recipe_id: int):
    db_recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not db_recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    db.delete(db_recipe)
    db.commit()
    return {"message": "Recipe deleted successfully"}

def read_all(db: Session):
    return db.query(Recipe).all()

def read_one(db: Session, recipe_id: int):
    db_recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db_recipe
