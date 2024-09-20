.PHONY: tests docs

dependencies: 
	@echo "Initializing Git..."
	git init
	@echo "Installing dependencies..."
	poetry install
	poetry run pre-commit install

env: dependencies
	@echo "Activating virtual environment..."
	poetry shell

tests:
	pytest

docs:
	@echo Save documentation to docs... 
	pdoc {{cookiecutter.directory_name}} -o docs --force
	@echo View API documentation... 
	pdoc {{cookiecutter.directory_name}} --http localhost:8080