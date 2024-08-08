install:
	pip install -r requirements.txt

install-no-cache:
	pip install --no-cache-dir -r requirements.txt

dev: 
	cd src && uvicorn main:app --reload
