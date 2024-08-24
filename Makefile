install:
	uv pip install -r pyproject.toml

migration-up:
	uv run alembic upgrade heads

migration-down:
	uv run alembic downgrade base

migration-create:
	uv run alembic revision -m "$(name)"

migration-history:
	uv run alembic history

migration-generate:
	uv run alembic revision --autogenerate -m "$(name)"

lint:
	uv run ruff check

lint-fix:
	uv run ruff check --fix

test:
	uv run pytest

check-types:
	uv run pyright

format:
	uv run ruff format

dev:
	uv run uvicorn app.main:app --reload

start:
	uv run fastapi run app/main.py

pre-commit:
	pre-commit run --all-files

docker-api:
	docker-compose up api --build
