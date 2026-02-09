# Install Fastapi and Uvicorn using PIP
# pip install fastapi uvicorn

from fastapi import FastAPI

# Create FastAPI app instance
app = FastAPI()

# Define a simple GET endpoint
@app.get("/")
def read_root():
    return {"message": "Hello World"}

# To run the app, use the command:
# uvicorn sample1:app --reload  

# That’s it! You have successfully set up FastAPI, created your first API endpoint, and can now run your application. When you navigate to http://localhost:8000, you should see the JSON response: {"message": "Hello World"}
# You can also access the automatically generated API documentation at http://localhost:8000/docs.