import PyPDF2
pdf = open("book.pdf", "rb")
reader = PyPDF2.PdfReader(pdf)
page_number=int(input("Enter the page to be extracted : "))
page = reader.pages[page_number]
print(page.extract_text())