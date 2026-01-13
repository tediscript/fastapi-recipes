# Hello World - Simple FastAPI JSON API

This is the simplest possible FastAPI recipe that demonstrates returning a JSON response.

## Features

- **Minimal Dependencies**: Only FastAPI and Uvicorn required
- **Single Endpoint**: `GET /` returns a JSON message
- **Auto-Documentation**: Visit `/docs` for interactive API docs
- **Production-Ready**: Follows FastAPI best practices

## Installation

```bash
make install
```

## Running the Server

```bash
make run
```

Server starts on `http://localhost:8000`

## Testing the API

### Using curl
```bash
curl http://localhost:8000/
```

**Expected Response:**
```json
{
  "message": "Hello World!"
}
```

### Using browser
Visit `http://localhost:8000/` to see the JSON response.

### Interactive API Documentation
Visit `http://localhost:8000/docs` to explore the interactive Swagger UI documentation.

## Code Explanation

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World!"}
```

- **FastAPI()**: Creates the application instance
- **@app.get("/")**: Decorator that defines a GET endpoint at the root path
- **async def read_root()**: Async function that handles the request
- **return {"message": "Hello World!"}**: FastAPI automatically converts this dict to JSON

## Key Concepts Demonstrated

1. **Routing**: How to define endpoints using decorators
2. **JSON Serialization**: FastAPI automatically converts Python dicts to JSON
3. **Async Support**: Using async functions for non-blocking operations
4. **Type Hints**: FastAPI leverages Python type hints for validation (not shown in this simple example, but important concept)

## Make Commands

```bash
make help     # Show all available commands
make install  # Install dependencies
make run      # Start the server
make test     # Run tests
make clean    # Clean up generated files
```

## Next Steps

- Try adding more endpoints with different paths
- Add path parameters and query parameters
- Explore Pydantic models for request/response validation
- Check out the `hello-world-html` recipe for server-side rendering
