#!/bin/bash

echo "Running tests..."

# Exit immediately if a command exits with a non-zero status
set -e  

# Run unit tests using pytest (or another testing framework)
pytest

# Run integration tests (if applicable)
# Example: python -m unittest discover tests/

echo "All tests passed successfully!"
