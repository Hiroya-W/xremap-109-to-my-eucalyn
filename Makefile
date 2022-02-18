FORMATTER := poetry run black
LINTER := poetry run flake8
IMPORT_SORTER := poetry run isort
TYPE_CHECKER := poetry run mypy

PROJECT_DIR := myxremap
CHECK_DIR := $(PROJECT_DIR) config.py

.PHONY: check
check: format lint type

.PHONY: format
format:
	$(FORMATTER) $(CHECK_DIR)
	$(IMPORT_SORTER) $(CHECK_DIR)

.PHONY: lint
lint:
	$(LINTER) $(CHECK_DIR)

.PHONY: type
type:
	$(TYPE_CHECKER) $(CHECK_DIR)
