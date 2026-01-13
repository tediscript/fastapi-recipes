# Hello World HTML - FastAPI Server-Side Rendering

This recipe demonstrates how to use FastAPI with Jinja2 templates to render HTML pages on the server.

## Features

- **Server-Side Rendering**: Uses Jinja2Templates for dynamic HTML generation
- **Beautiful UI**: Modern, responsive design with gradient background
- **Template Engine**: Integrates Jinja2 for flexible templating
- **Request Context**: Passes request object to templates for URL generation
- **Production-Ready**: Follows FastAPI best practices for HTML responses

## Installation

1. Navigate to the recipe directory:
```bash
cd hello-world-html
```

2. Create a virtual environment:
```bash
make venv
```

3. Install dependencies:
```bash
make install
```

## Running the Server

Start the server using make:

```bash
make run
```

Or run directly with uvicorn:

```bash
uvicorn main:app --reload
```

Or run the main.py directly:
```bash
python main.py
```

The server will start on `http://localhost:8000`

## Testing

### Using browser
Visit `http://localhost:8000/` to see the rendered HTML page.

### Interactive API Documentation
Visit `http://localhost:8000/docs` to explore the interactive Swagger UI documentation.

## Code Explanation

### main.py
```python
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "message": "Hello World!"}
    )
```

**Key Components:**

- **Jinja2Templates**: Template engine instance configured to look in the `templates` directory
- **HTMLResponse**: Response class that tells FastAPI to return HTML instead of JSON
- **Request object**: Required by FastAPI templates for URL generation and context
- **TemplateResponse**: Renders the template with the provided context dictionary

### templates/index.html
```html
<div class="message">{{ message }}</div>
```

- **Jinja2 syntax**: `{{ message }}` is replaced with the value from the context
- **Dynamic content**: You can pass any Python data to templates and display them

## Key Concepts Demonstrated

1. **Template Engine Setup**: How to configure Jinja2Templates with FastAPI
2. **HTMLResponse**: Returning HTML instead of JSON
3. **Request Object**: Why templates need the request object
4. **Template Context**: Passing data from Python to HTML templates
5. **Jinja2 Syntax**: Basic variable interpolation in templates

## Template Features

The included `index.html` template demonstrates:

- **CSS Styling**: Inline styles for a modern, responsive design
- **Animation**: Fade-in effect on page load
- **Responsive Layout**: Works on mobile and desktop
- **Gradient Background**: Modern visual design
- **Jinja2 Integration**: Dynamic content injection

## Common Use Cases for SSR

Server-Side Rendering with FastAPI is ideal for:

- **Traditional web applications**: Pages that need to be SEO-friendly
- **Email templates**: Generating HTML emails
- **Admin dashboards**: Backend interfaces
- **Static site generation**: Pre-rendering content
- **Hybrid applications**: Mixing API and web routes

## Next Steps

- Try adding more dynamic data to templates (loops, conditionals)
- Create multiple templates and extend them with Jinja2 inheritance
- Add template filters and custom functions
- Integrate with databases to display real data
- Add user authentication and protected routes
- Check out the simple `hello-world` recipe for JSON API basics

## Comparison with JSON API

| Feature | JSON API | HTML SSR |
|---------|----------|----------|
| Best for | APIs, SPAs | Traditional web apps |
| Response | JSON data | Rendered HTML |
| SEO | Limited | Excellent |
| Client | JavaScript-heavy | Any browser |
| Complexity | Simpler | More complex |
| Use case | Mobile apps, React/Vue | Static sites, email, admin |

## Resources

- [FastAPI Templates Documentation](https://fastapi.tiangolo.com/advanced/templates/)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/)
- [FastAPI HTMLResponse](https://fastapi.tiangolo.com/advanced/custom-response/)
