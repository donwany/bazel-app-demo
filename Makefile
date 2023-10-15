test:
	python -m pytest -vs test/*.py
coverage:
	python -m pytest --cov=main

isort:
	python -m isort main/*.py

format:
	python -m black main/*.py

# Add a 'clean' target to remove any generated test artifacts
clean:
	rm -rf __pycache__ .pytest_cache

# Add a 'help' target to display available make targets
help:
	@echo "Available targets:"
	@echo "  test     - Run tests using pytest"
	@echo "  clean    - Remove generated test artifacts"
	@echo "  help     - Display this help message"

# Prevent make from failing when the 'clean' target is missing
.PHONY: test clean help
