from pypdf import PdfReader
import os

def load_pdf(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"file not found :{file_path}"
        )
    reader=PdfReader(file_path)
    pages=[]
    for page_number,page in enumerate(reader.pages,start=1):
        text=page.extract_text()
        text=text or ""
        pages.append(
            {
                "source":os.path.basename(file_path),
                "page":page_number,
                "text":text
            }
        )
        return pages
    