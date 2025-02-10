# Num-Classification-Api

A simple API for classifying numbers using FastAPI.

# Table of Contents
- #about
- #features
- #requirements
- #installation
- #usage
- #api-endpoint
- #api-documentation
- #contributing
- #license

# About
This API provides a simple endpoint for classifying numbers into different categories.

# Features
- Classify numbers into different categories (e.g., even, odd, prime)

# Requirements
- Python 3.9+
- FastAPI
- Uvicorn

# Installation
To install the required dependencies, run:

bash
pip install fastapi uvicorn


# Usage
To start the API, run:

bash
uvicorn app:app --host 0.0.0.0 --port 8000

You can then access the API at http://localhost:8000/.

# API Endpoint
You can access the number classification API at:

https://num-classification-api-3.onrender.com/api/classify-number/?number={number}

Replace {number} with the number you want to classify.

# API Documentation
API documentation is available at http://localhost:8000/docs.

# Contributing
Contributions are welcome! Please submit a pull request with your changes.

# License
This project is licensed under the MIT License. See LICENSE.txt for details.
