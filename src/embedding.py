## import modules
from openai import OpenAI
from dotenv import load_dotenv

## Load Environment
load_dotenv()

class OpenAIEmbeddingService:
    def __init__(self):
        self.client=OpenAI()

    def generate_embdding(self,chunks):
        texts=[chunk["text"] for chunk in chunks]
        response=self.client.embeddings.create(
            model="text-embedding-3-small",
            input=texts
        )

        for chunk,embedding in zip(chunks,response.data):
            chunk["embedding"]=embedding.embedding
        return chunks
    def embed_query(self,query):
        response=self.client.embeddings.create(
            model="text-embedding-3-small",
            input=query
        )
        return response.data[0].embedding





