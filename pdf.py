import os
from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter

def create_pdf(reader, name):
    return {"pdf": reader, "name": name, "pages": len(reader.pages)}

pdfPari = create_pdf(PdfReader(input("Name of pdf file with even page numbers: ")), "pari")
pdfDispari = create_pdf(PdfReader("Name of pdf file with even page numbers: "), "dispari")

def merge_pdf(pari, dispari):
    if os.path.exists("merged.pdf"):
        print("merged.pdf already exists, removing it")
        os.remove("merged.pdf")

    print("pdf pari pages = " + str(dispari["pages"]))
    print("pdf dispari pages = " + str(pari["pages"]))

    writer = PdfWriter()
    for i in range(pdfDispari["pages"]):
        writer.add_page(dispari["pdf"].pages[i])
        writer.add_page(pari["pdf"].pages[pari["pages"] - i - 1])
    
    writer.write("merged.pdf")

merge_pdf(pdfPari, pdfDispari)
