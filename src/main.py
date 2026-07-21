from pdf_loader import load_pdf
from chunker import create_chunks
from embedding import OpenAIEmbeddingService
from vector_store import Vector_Store
from llm import LLMService

PDF_Path="Data/NovaTech_Employee_Handbook.pdf"
pages=load_pdf(PDF_Path)
chunks=create_chunks(pages)
embedding_service=OpenAIEmbeddingService()
embeded_chunk=embedding_service.generate_embdding(chunks)

print("="*60)
print("Enterprise RAG System")
print("="*60)

print(f"Total Pages : {len(pages)}")
print()
print("First Page Perview")
print("-"*60)
print(pages[0]["text"][:500])

print("="*60)
print("Chunk Statistics")
print("="*60)
print(f"Total Pages : {len(pages)}")
print(f"Total Chunk : {len(chunks)}")
print("\n First Chunk")
print("-"*60)
print(chunks[0]["text"])

print("="*60)
print("Embedding Statistics")
print("="*60)
print(f"Embedded Chunks : {len(embeded_chunk)}")
print()
print("Embedding Dimension")
print(len(embeded_chunk[0]["embedding"]))
vs=Vector_Store()
vs.built_index(embeded_chunk)
print()

query = "How many vacation days do employees receive?"
print("="*60)
print("User Query")
print("="*60)
print(query)

query_embedding=embedding_service.embed_query(query)
results=vs.search(
    query_embedding=query_embedding,
    top_k=3
)

print("\n"+"="*60)
print("Search Result ")
print("="*60)

for rank,chunk in enumerate(results,start=1):
    print(f"\nRank : {rank}")
    print(f"Source : {chunk['source']}")
    print(f"Page   : {chunk['page']}")
    print("-" * 60)
    print(chunk["text"])

context=""
for chunk in results:
    context+=chunk["text"]+"\n\n"
llm=LLMService()
answer=llm.generate_answer(
    query,
    context
)
print("="*60)
print("AI Answer")
print("="*60)
print(answer)