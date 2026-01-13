# FastAPI Recipes

[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A collection of ready-to-use recipes and patterns for building applications with FastAPI.

## About

This repository serves as a practical cookbook for FastAPI developers, providing reusable code snippets, patterns, and complete examples for common use cases. Each recipe is designed to be easily integrated into your projects or used as a learning reference.

## Features

- 🚀 **Production-Ready Patterns**: Battle-tested implementations for real-world scenarios
- 📦 **Modular Design**: Each recipe is self-contained and easy to understand
- 🔧 **Customizable**: Adaptable to fit your specific requirements
- 📚 **Well-Documented**: Clear explanations and usage examples
- 🧪 **Tested**: Code that you can trust

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip or poetry package manager

### Installation

Clone the repository:

```bash
git clone https://github.com/tediscript/fastapi-recipes.git
cd fastapi-recipes
```

Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies:

```bash
pip install fastapi uvicorn
```

## Recipes Structure

Recipes are organized by functionality and use case. Each recipe folder contains:

- `main.py` - The main implementation
- `requirements.txt` - Specific dependencies (if any)
- `README.md` - Detailed documentation
- `tests/` - Example tests (if applicable)

```
fastapi-recipes/
├── recipes/
│   ├── recipe-name-1/
│   ├── recipe-name-2/
│   └── ...
├── README.md
└── ...
```

## Requirements

### Core Dependencies

- **FastAPI** (>= 0.100.0) - Modern, fast web framework for building APIs
- **Uvicorn** (>= 0.23.0) - Lightning-fast ASGI server
- **Pydantic** (>= 2.0.0) - Data validation using Python type annotations

### Optional Dependencies

Depending on the recipe, you may need:
- `sqlalchemy` - SQL toolkit and ORM
- `databases` - Async database support
- `httpx` - Async HTTP client
- `python-jose` - JWT token handling
- `passlib` - Password hashing
- And more (recipe-specific)

## Running a Recipe

Navigate to any recipe directory and run:

```bash
uvicorn main:app --reload
```

Then visit `http://localhost:8000/docs` to explore the interactive API documentation.

## Resources

- [FastAPI Official Documentation](https://fastapi.tiangolo.com/)
- [FastAPI GitHub Repository](https://github.com/tiangolo/fastapi)
- [Uvicorn Documentation](https://www.uvicorn.org/)
