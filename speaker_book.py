import pyttsx3
import PyPDF2
book=open("SE.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
print(pages)
bot=pyttsx3.init()
voices=bot.getProperty('voices')
bot.setProperty('voice', voices[1].id) #[1].id:woman voice - [2].id
page=pdfReader.getPage(2) #lấy trang
text=page.extractText()
bot.say(text)
bot.runAndWait()

bot.setProperty('rate', 125)     # setting up new voice rate