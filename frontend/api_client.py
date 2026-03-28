# All communication with the  backend lives here.

import os
import requests

# Set BACKEND_URL env var when deploying (e.g. https://example-api.railway.app)
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")


def generate_headlines(article: str, creativity: float, tone: str) -> list[dict]:
    """
    Call POST /generate on the backend and return a list of model result dicts.

    Raises
    ------
    RuntimeError if the request fails or the backend returns an error.
    """
    payload = {
        "article":    article,
        "creativity": creativity,
        "tone":       tone,
    }

    try:
        response = requests.post(
            f"{BACKEND_URL}/generate",
            json=payload,
            timeout=30,
        )
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        raise RuntimeError(
            f"Cannot reach backend at {BACKEND_URL}. "
            "Make sure the backend is running and BACKEND_URL is set correctly."
        )
    except requests.exceptions.HTTPError as e:
        raise RuntimeError(f"Backend returned an error: {e}")

    return response.json()["results"]