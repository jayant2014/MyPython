import pyttsx3
import PyPDF2
book = open('Stories.pdf', 'rb')
#book = open('Hooked_In_Real_Life_ebook.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(book)
num_pages = pdf_reader.getNumPages()
print("Number of pages in document : ", num_pages)

speaker = pyttsx3.init()
for index in range(1, num_pages):
    page = pdf_reader.getPage(index)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
