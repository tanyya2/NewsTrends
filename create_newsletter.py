import requests
from google import genai

geminiAPIKey = "REDACTED"

gemini = genai.Client(
  api_key=geminiAPIKey
)
