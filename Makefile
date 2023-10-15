test:
	python -m pytest -vs test/*.py

coverage:
	coverage run -m pytest test/*.py

isort:
	python -m isort main/*.py

format:
	python -m black main/*.py

lint:
	python -m pylint main/*.py

# Add a 'clean' target to remove any generated test artifacts
clean:
	rm -rf __pycache__ .pytest_cache

# Add a 'help' target to display available make targets
help:
	@echo "Available targets:"
	@echo "  test     - Run tests using pytest"
	@echo "  clean    - Remove generated test artifacts"
	@echo "  format   - Format codes"
	@echo "  isort    - sorts imports"
	@echo "  lint     - format with lint"
	@echo "  help     - Display this help message"

# Prevent make from failing when the 'clean' target is missing
.PHONY: test clean format isort lint help
