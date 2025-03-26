from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import Sandwich
from schemas import SandwichCreate, SandwichUpdate

def create_sandwich(db: Session, sandwich: SandwichCreate):
    db_sandwich = Sandwich(**sandwich.dict())
    db.add(db_sandwich)
    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich

def get_sandwiches(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Sandwich).offset(skip).limit(limit).all()

def get_sandwich_by_id(db: Session, sandwich_id: int):
    return db.query(Sandwich).filter(Sandwich.id == sandwich_id).first()

def update_sandwich(db: Session, sandwich_id: int, sandwich: SandwichUpdate):
    db_sandwich = db.query(Sandwich).filter(Sandwich.id == sandwich_id).first()
    if db_sandwich:
        for key, value in sandwich.dict(exclude_unset=True).items():
            setattr(db_sandwich, key, value)
        db.commit()
        db.refresh(db_sandwich)
        return db_sandwich
    raise HTTPException(status_code=404, detail="Sandwich not found")

def delete_sandwich(db: Session, sandwich_id: int):
    db_sandwich = db.query(Sandwich).filter(Sandwich.id == sandwich_id).first()
    if db_sandwich:
        db.delete(db_sandwich)
        db.commit()
        return {"message": "Sandwich deleted successfully"}
    raise HTTPException(status_code=404, detail="Sandwich not found")
