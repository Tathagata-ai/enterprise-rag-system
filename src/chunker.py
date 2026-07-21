def create_chunks(pages,chunk_size=500):
    chunks=[]
    chunk_id=1

    for page in pages:
        text=page["text"]
        for i in range(0,len(text),chunk_size):
            chunk=text[i:i+chunk_size]
            chunks.append({
                "chunk_id":chunk_id,
                "source":page["source"],
                "page":page["page"],
                "text":chunk
            })
            chunk_id+=1
    return chunks
