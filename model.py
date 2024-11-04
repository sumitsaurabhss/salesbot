import os
from langchain_google_genai import ChatGoogleGenerativeAI
from config import GEMINI_API_KEY

# Define and configure the LLM model
os.environ['GOOGLE_API_KEY'] = GEMINI_API_KEY

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0,
    max_tokens=None
)
