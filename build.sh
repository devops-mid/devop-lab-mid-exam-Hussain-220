#!/bin/bash

echo "Building the application..."

# Exit immediately if a command exits with a non-zero status
set -e  

# Install dependencies
pip install -r requirements.txt

# Additional setup steps if required
echo "Build completed successfully!"
