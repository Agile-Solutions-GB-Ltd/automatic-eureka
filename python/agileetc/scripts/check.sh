#!/usr/bin/env bash
#
# check.sh - Check that we can commit this project locally.

poetry run flake8
poetry run pytest
