import os
from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter

def create_pdf(reader, name):
    return {"pdf": reader, "name": name, "pages": len(reader.pages)}

pdfEven = create_pdf(PdfReader(input("Name of pdf file with even page numbers: ")), "even")
pdfOdd = create_pdf(PdfReader(input("Name of pdf file with even page numbers: ")), "odd")

def merge_pdf(even, odd):
    if os.path.exists("merged.pdf"):
        print("merged.pdf already exists, removing it")
        os.remove("merged.pdf")

    print("PDF even pages = " + str(odd["pages"]))
    print("PDF odd pages = " + str(even["pages"]))

    writer = PdfWriter()
    for i in range(pdfOdd["pages"]):
        writer.add_page(odd["pdf"].pages[i])
        writer.add_page(even["pdf"].pages[even["pages"] - i - 1])
    
    writer.write("merged.pdf")

merge_pdf(pdfEven, pdfOdd)
