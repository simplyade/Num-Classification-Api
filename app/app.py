"""
Number Classification API

This API classifies numbers into different categories such as prime, perfect, armstrong, etc.
It also provides a fun fact about the number.

Endpoints:
    GET /api/classify-number/?number=<number>
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from .classifier.number_classifier import classify_number
from .classifier.utils import get_fun_fact

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/")
@app.get("/api/classify-number/")
async def api_classify_number(number: str = Query(None)):
    """
    Classify a number and return its classification and fun fact.

    Args:
        number (str): The number to classify. Defaults to None.

    Returns:
        dict: A dictionary containing the number's classification and fun fact.
    """
    try:
        if number is None:
            raise HTTPException(status_code=400, detail={"number": "alphabet", "error": True})

        # Remove quotes from the input number
        number = number.strip('"\'')

        # Check if the input is a valid integer
        if not number.lstrip('-').isdigit():
            raise HTTPException(status_code=400, detail={"number": "alphabet", "error": True})

        number = int(number)
        result = classify_number(number)
        result['fun_fact'] = await get_fun_fact(number)
        return result
    except HTTPException as e:
        raise e
    except Exception as e:
        return {"number": "alphabet", "error": True}
