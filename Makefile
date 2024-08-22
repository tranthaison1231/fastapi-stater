install:
	pip install -r requirements/base.txt

install-no-cache:
	pip install --no-cache-dir -r requirements/base.txt

migration-up:
	alembic upgrade heads

migration-down:
	alembic downgrade base

migration-create:
	alembic revision -m "$(name)"

migration-history:
	alembic history

migration-generate:
	alembic revision --autogenerate -m "$(name)"

lint:
	ruff check

lint-fix:
	ruff check --fix

test:
	pytest

check-types:
	pyright

check-updates:
	pip list --outdated	

format:
	ruff format

dev: 
	uvicorn app.main:app --reload 

pre-commit:
	pre-commit run --all-files

docker-api:
	docker-compose up api
