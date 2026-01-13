.PHONY: help venv install run clean

# Variables
PYTHON := python3
VENV := venv
VENV_BIN := $(VENV)/bin
REQUIREMENTS := requirements.txt
APP_MODULE := main:app
HOST := 0.0.0.0
PORT := 8000

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

venv: ## Create virtual environment
	$(PYTHON) -m venv $(VENV)

install: venv ## Install dependencies (creates venv if needed)
	$(VENV_BIN)/pip install --upgrade pip
	$(VENV_BIN)/pip install -r $(REQUIREMENTS)

run: ## Run the development server
	$(VENV_BIN)/uvicorn $(APP_MODULE) --host $(HOST) --port $(PORT) --reload

clean: ## Clean up generated files
	find . -type d -name '__pycache__' -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.pyo' -delete
	find . -type f -name '*.pyd' -delete
	rm -rf $(VENV)
