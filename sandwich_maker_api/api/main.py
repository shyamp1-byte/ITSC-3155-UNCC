from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from .models import models, schemas
from .controllers import orders, sandwiches, resources
from .dependencies.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/orders/", response_model=schemas.Order, tags=["Orders"])
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return orders.create(db=db, order=order)


@app.get("/orders/", response_model=list[schemas.Order], tags=["Orders"])
def read_orders(db: Session = Depends(get_db)):
    return orders.read_all(db)


@app.get("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def read_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order


@app.put("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def update_one_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    order_db = orders.read_one(db, order_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.update(db=db, order=order, order_id=order_id)


@app.delete("/orders/{order_id}", tags=["Orders"])
def delete_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.delete(db=db, order_id=order_id)


@app.post("/sandwiches/", response_model=schemas.Sandwich, tags=["Sandwiches"])
def create_sandwich_endpoint(sandwich: schemas.SandwichCreate, db: Session = Depends(get_db)):
    return sandwiches.create_sandwich(db=db, sandwich=sandwich)

@app.get("/sandwiches/", response_model=list[schemas.Sandwich], tags=["Sandwiches"])
def get_sandwiches_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return sandwiches.get_sandwiches(db=db, skip=skip, limit=limit)

@app.get("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich, tags=["Sandwiches"])
def get_sandwich_endpoint(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich = sandwiches.get_sandwich(db=db, sandwich_id=sandwich_id)
    if sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return sandwich

@app.put("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich, tags=["Sandwiches"])
def update_sandwich_endpoint(sandwich_id: int, sandwich: schemas.SandwichUpdate, db: Session = Depends(get_db)):
    sandwich_db = sandwiches.get_sandwich(db=db, sandwich_id=sandwich_id)
    if sandwich_db is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return sandwiches.update_sandwich(db=db, sandwich=sandwich, sandwich_id=sandwich_id)

@app.delete("/sandwiches/{sandwich_id}", tags=["Sandwiches"])
def delete_sandwich_endpoint(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich = sandwiches.get_sandwich(db=db, sandwich_id=sandwich_id)
    if sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return sandwiches.delete_sandwich(db=db, sandwich_id=sandwich_id)


@app.post("/resources/", response_model=schemas.Resource, tags=["Resources"])
def create_resource_endpoint(resource: schemas.ResourceCreate, db: Session = Depends(get_db)):
    return resources.create_resource(db=db, resource=resource)

@app.get("/resources/", response_model=list[schemas.Resource], tags=["Resources"])
def get_resources_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return resources.get_resources(db=db, skip=skip, limit=limit)

@app.get("/resources/{resource_id}", response_model=schemas.Resource, tags=["Resources"])
def get_resource_endpoint(resource_id: int, db: Session = Depends(get_db)):
    resource = resources.get_resource(db=db, resource_id=resource_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resource

@app.put("/resources/{resource_id}", response_model=schemas.Resource, tags=["Resources"])
def update_resource_endpoint(resource_id: int, resource: schemas.ResourceUpdate, db: Session = Depends(get_db)):
    resource_db = resources.get_resource(db=db, resource_id=resource_id)
    if resource_db is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resources.update_resource(db=db, resource=resource, resource_id=resource_id)

@app.delete("/resources/{resource_id}", tags=["Resources"])
def delete_resource_endpoint(resource_id: int, db: Session = Depends(get_db)):
    resource = resources.get_resource(db=db, resource_id=resource_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resources.delete_resource(db=db, resource_id=resource_id)
