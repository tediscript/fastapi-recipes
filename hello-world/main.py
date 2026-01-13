from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    """
    Returns a simple Hello World message in JSON format.
    
    This is the simplest FastAPI example demonstrating:
    - Basic routing with @app.get()
    - Automatic JSON serialization
    - Async function support
    """
    return {"message": "Hello World!"}


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
