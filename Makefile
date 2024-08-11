install:
	pip install -r requirements/base.txt

install-no-cache:
	pip install --no-cache-dir -r requirements/base.txt

migration-up:
	cd app && alembic upgrade heads

migration-down:
	cd app && alembic downgrade base

migration-create:
	cd app && alembic revision -m "$(name)"

migration-generate:
	cd app && alembic revision --autogenerate -m "$(name)"

lint:
	ruff check

lint-fix:
	ruff check --fix

check-types:
		pyright

format:
	ruff format

dev: 
	cd app && python main.py 

docker-api:
	docker-compose up api
