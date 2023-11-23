install:
	poetry install

# install-dev:
# 	poetry install --with dev

run:
	poetry run python confluence_space_cloner/main.py