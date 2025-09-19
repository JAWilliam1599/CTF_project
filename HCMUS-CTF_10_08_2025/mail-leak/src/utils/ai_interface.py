import requests
import os
from dotenv import load_dotenv
from typing import Dict, Any, List

load_dotenv()


class Config:
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    MODEL_NAME = os.getenv("MODEL_NAME", "google/gemini-pro")
    BASE_URL = os.getenv("BASE_URL", "https://openrouter.ai/api/v1")

    OPENROUTER_HEADERS = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    REQUEST_TIMEOUT = 30

    MAX_PROMPT_LENGTH = 1000


class AIInterface:
    def __init__(self):
        self.headers = Config.OPENROUTER_HEADERS
        self.base_url = Config.BASE_URL
        self.model = Config.MODEL_NAME

    def validate_response(self, response: Dict[str, Any]) -> bool:
        if not response.get("choices"):
            raise ValueError("Invalid response structure: missing 'choices'")
        if not response["choices"][0].get("message"):
            raise ValueError("Invalid response structure: missing 'message'")
        if not response["choices"][0]["message"].get("content"):
            raise ValueError("Invalid response structure: missing 'content'")
        return True

    def send_prompt(
        self, prompt: List[str], system_prompt: str = None
    ) -> Dict[str, Any]:
        messages = []

        if system_prompt:
            messages.append({"role": "system", "content": system_prompt.strip()})

        # Handle list of strings - first message is user prompt
        if not isinstance(prompt, list) or not prompt:
            raise ValueError("Prompt must be a non-empty list")

        # First message is always user
        first_prompt = prompt[0].strip()
        if not first_prompt:
            raise ValueError("Empty prompt received")

        if len(first_prompt) > Config.MAX_PROMPT_LENGTH:
            raise ValueError(
                f"Prompt exceeds maximum length of {Config.MAX_PROMPT_LENGTH} characters"
            )

        messages.append({"role": "user", "content": first_prompt})

        # Additional messages alternate between assistant and user
        for i, msg in enumerate(prompt[1:], 1):
            role = "assistant" if i % 2 == 1 else "user"
            messages.append({"role": role, "content": msg.strip()})

        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 1000,
            "presence_penalty": 0.6,
        }

        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=self.headers,
                json=payload,
                timeout=Config.REQUEST_TIMEOUT,
            )
            response.raise_for_status()

            result = response.json()
            self.validate_response(result)

            result_content = result["choices"][0]["message"]["content"]

            return {
                "content": result_content,
                "usage": result.get("usage", {}),
                "model": result.get("model", self.model),
                "messages": messages,  # Return the full conversation context
            }

        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")
        except ValueError as e:
            raise Exception(f"Response validation failed: {str(e)}")
        except Exception as e:
            raise Exception(f"Unexpected error: {str(e)}")
