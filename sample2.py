# This is a sample FastAPI application.
# To run this application, save it as sample2.py and use the command:
# uvicorn sample2:app --reload  


from fastapi import FastAPI

app = FastAPI()

# Define a simple GET endpoint that returns a JSON response.
# You can access this endpoint by navigating to http://localhost:8000/ in your web browser or using a tool like curl or Postman.
@app.get("/")
async def read_root():
    return {"Hello": "World"}

# This endpoint will return the item_id and an optional query parameter q.
# You can access it by navigating to http://localhost:8000/items/5?q=somequery
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}