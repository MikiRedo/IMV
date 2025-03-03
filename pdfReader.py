import fitz 

def pdfRedaer(pdfLink, keywords):
    doc = fitz.open(pdfLink)
    text = ""

    for page in pdfLink:
        text += page.get_text()

    return()

    