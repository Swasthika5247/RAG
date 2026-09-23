from dotenv import load_dotenv
import os
from langchain_openrouter import ChatOpenRouter
load_dotenv()

model = ChatOpenRouter(
    model="meta-llama/llama-3.3-70b-instruct",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0.1
)
#response = model.invoke()
#print(response)