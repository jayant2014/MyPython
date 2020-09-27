import PyPDF2

pdf_reader = PyPDF2.PdfFileReader('Hooked_In_Real_Life_ebook.pdf')
print(pdf_reader.documentInfo)
pages = pdf_reader.getNumPages()

text = ""
for page in range(1, pages):
    text += pdf_reader.getPage(page).extractText()

with open("text.txt", "w", encoding='utf-8') as f:
    f.write(text)
