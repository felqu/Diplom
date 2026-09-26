.PHONY: up down test lint

up:
	docker compose up --build

down:
	docker compose down

test:
	pytest services/*/tests apps/*/tests

lint:
	ruff check apps services libs
