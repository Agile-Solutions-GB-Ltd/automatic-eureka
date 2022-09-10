#!/usr/bin/env bash
#
# release.sh - Release package.

poetry version patch
poetry publish --build --username $PYPI_USERNAME --password $PYPI_PASSWORD