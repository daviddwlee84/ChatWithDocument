from langchain.embeddings.openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv('../.env')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# https://python.langchain.com/en/latest/reference/modules/embeddings.html?highlight=OpenAIEmbeddings#langchain.embeddings.OpenAIEmbeddings
# Default model: text-embedding-ada-002
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

query_result = embeddings.embed_query('This is a test query')
print(query_result)
print(type(query_result))  # <class 'list'>
print(len(query_result))  # 1536
import ipdb
ipdb.set_trace()
