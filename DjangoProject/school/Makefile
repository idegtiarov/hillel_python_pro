lint:
	flake8 --docstring-convention --verbose

test:
	pytest

format:
	black .

test_all:
	make format
	make lint
	make test
