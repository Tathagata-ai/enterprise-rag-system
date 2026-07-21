import faiss
import numpy as np

class Vector_Store:
    def __init__(self):
        self.index=None
        self.chunks=None
    def built_index(self,chunks):
        self.chunks=chunks

        embeddings=np.array(
            [chunk["embedding"] for chunk in chunks],
            dtype=np.float32
        )
        dimension=embeddings.shape[1]
        self.index=faiss.IndexFlatL2(dimension)
        self.index.add(embeddings)
        print(f"Indexed {len(chunks)} chunks.")
    def search(self,query_embedding,top_k=3):
        query_vector=np.array(
            [query_embedding],
            dtype=np.float32
        )
        distances,indices=self.index.search(
            query_vector,
            top_k
        )
        results=[]
        for index in indices[0]:
            results.append(self.chunks[index])
        return results
    
        

