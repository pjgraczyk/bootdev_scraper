#!/bin/sh

# Activate env
. ./.venv/bin/

#Run tests
uv run -m unittest -v
