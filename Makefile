# Variables
APP_NAME=app
MODULE=main:app
PORT=8000
DOCKER_IMAGE=fastapi-app
PYTHON=python3

# Environment setup
.PHONY: install
install:
	pip install -r requirements.txt

# Run the FastAPI server
.PHONY: run
run:
	uvicorn $(MODULE) --host 0.0.0.0 --port $(PORT) --reload