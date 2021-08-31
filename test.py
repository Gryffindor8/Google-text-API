import os
import sys

import docx
import requests


def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)


info = requests.get("http://theangrynerds.com/media/FA17-BSE-086.pdf")

print(info.text)
book = (info.json())
print("Estimated size: " + str(sys.getsizeof(book) / 1024) + "KB")

b = (book[0])
dc = (b["Pdfstore"])
print(getText(dc))
