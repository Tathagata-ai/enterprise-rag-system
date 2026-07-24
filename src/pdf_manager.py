from pathlib import Path
from pdf_loader import load_pdf

class PDFManager:
    def __init__(self,data_folder):
        self.data_folder=Path(data_folder)
    def load_all_pdfs(self):
        all_pages=[]
        pdf_files=sorted(self.data_folder.glob("*.pdf"))
        print(f"\n Found {len(pdf_files)} PDF(s)\n ")

        for pdf_file in pdf_files:
            print(f"Loading: {pdf_file.name}")
            pages=load_pdf(str(pdf_file))
            all_pages.extend(pages)
        print("=" * 50)
        print(f"Total Pages Loaded : {len(all_pages)}")
        print("=" * 50)
        return all_pages
    



