#from pdf_loader import load_pdf
#from pdf_manager import PDFManager
#from chunker import create_chunks
from embedding import OpenAIEmbeddingService
from vector_store import Vector_Store
from llm import LLMService

#---------------------------------------------
# Build Knowledge Base
#---------------------------------------------
'''print("Building knowledge base")
print("--------------------------------------")
#PDF_PATH="Data/NovaTech_Employee_Handbook.pdf"
DATA_FOLDER="Data"
pdf_manager=PDFManager(DATA_FOLDER)
print("Loading PDF.....")
#pages=load_pdf(PDF_PATH)
pages=pdf_manager.load_all_pdfs()

print("Creating Chunks....")
chunks=create_chunks(pages)

print("Generating Embedding...")
embedding_service=OpenAIEmbeddingService()
embeded_chunks=embedding_service.generate_embdding(chunks)

print("Building FAISS index")
vs=Vector_Store()
vs.built_index(embeded_chunks)

print("Knowledge base ready....")
print("----------------------------------------")
print()'''

#-----------------------------------------
#Loading existing knowledgebase
#-----------------------------------------
print("Loading Knowledgebase....")
print("------------------------------------")
embedding_service=OpenAIEmbeddingService()
vs=Vector_Store()
vs.load_index(
    "indexes/faiss.index",
    "indexes/metadata.pkl"
)
print("Knowledge Base Loaded Successfully!")
print("--------------------------------------")
print()


#--------------------------------------------
# Initialize LLM
#--------------------------------------------
llm=LLMService()

print("\n" + "=" * 70)
print("Enterprise RAG Assistant")
print("=" * 70)
print("Type your question.")
print("Type 'exit' to quit.")
print("=" * 70)

while True:
    query=input("\n You :")
    if query.lower()=="exit":
        print("Good Bye...")
        break
    query_embedding=embedding_service.embed_query(query)
    results=vs.search(query_embedding)
    context=""
    for chunk in results:
        context+=chunk["text"]+"\n\n"
    answer=llm.generate_answer(query,context)

    print("\nAI :")
    print("-" * 60)
    print(answer)

    print("\nSources:")
    shown=set()
    for chunk in results:
        source=f"- {chunk['source']} (Page {chunk['page']})"

        if source not in shown:
            print(f"- {source}")
            shown.add(source)
    
    




