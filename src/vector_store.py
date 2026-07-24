import faiss
import numpy as np
import pickle

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
    
    
    def save_index(self,index_path,metadata_path):
        faiss.write_index(self.index,index_path)
        with open(metadata_path,"wb") as file:
            pickle.dump(self.chunks,file)
        print("Vector index saved successfully")

    def load_index(self,index_path,metadata_path):
        self.index=faiss.read_index(index_path)
        with open(metadata_path,"rb") as file:
            self.chunks=pickle.load(file)
        print("Vector index loaded successsfully")

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

    
        

