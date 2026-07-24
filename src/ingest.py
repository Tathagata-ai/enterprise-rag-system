from pathlib import Path
from pdf_manager import PDFManager
from chunker import create_chunks
from embedding import OpenAIEmbeddingService
from vector_store import Vector_Store

#------------------------------------------
# Configuration
#------------------------------------------
DATA_FOLDER="Data"
INDEX_FOLDER="indexes"
INDEX_FILE=f"{INDEX_FOLDER}/faiss.index"
METADATA_FILE=F"{INDEX_FOLDER}/metadata.pkl"

#---------------------------------------------
# Creating Index Folder
#---------------------------------------------
Path(INDEX_FOLDER).mkdir(exist_ok=True)

#---------------------------------------------
#Load PDF
#---------------------------------------------
pdf_manager=PDFManager(DATA_FOLDER)
pages=pdf_manager.load_all_pdfs()

#--------------------------------------------
#Create chunks
#--------------------------------------------
chunks=create_chunks(pages)
print(f"\nTotal Chunks :{len(chunks)}")

#-------------------------------------------
#  Generate Embeddings
#-------------------------------------------
embedding_service=OpenAIEmbeddingService()
embeded_chunks=embedding_service.generate_embdding(chunks)

#----------------------------------------------
#Built Vector Store
#----------------------------------------------
vs=Vector_Store()
vs.built_index(embeded_chunks)

#----------------------------------------
# Save Index
#------------------------------------------
vs.save_index(
    INDEX_FILE,
    METADATA_FILE
)

print(f"\n Knowledgebase created successfully..")



