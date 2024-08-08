install:
	pip install -r requirements.txt

install-no-cache:
	pip install --no-cache-dir -r requirements.txt

migrations-up:
	alembic upgrade heads

migrations-down:
	alembic downgrade base

migration-create:
	alembic revision -m "$(name)"

dev: 
	uvicorn app.main:app --reload
