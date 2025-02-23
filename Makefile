.PHONY: deploy format
deploy:
	git push amvera main:master

lint:
	uv run ruff check
	uv run ruff format
