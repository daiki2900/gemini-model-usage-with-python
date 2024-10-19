import google.generativeai as genai
import os

# Retrieve the API key from the environment variable
gemeini_api_key = os.getenv("GEMINI_API_KEY")

# Configure the GenAI library with the obtained API key
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create a GenerativeModel object
model = genai.GenerativeModel("gemini-1.5-flash")

# processe the prompt and generates a response
response = model.generate_content("What is Gemini API")
print(response.text)
