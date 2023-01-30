from reportLab.pdfgen import canvas

texto=['o patio']

aux=canvas.Canvas('pdfTexto.')





textoContinuo = '''texto'''

text.textLines(textoContinuo)

for i,tipoLetra in enumerate(aux.getAvailableFonts()):
    text.setFont(tipoLetra,14)
    text.textLines(tipoLetra,'''textLines''')
    text.moveCursor(20,25)
    text.setWordSpace(i*10)

text.setFillColorRGB(0,0,1)
text.setFont('Helvetica',12)
text.textLines('text color')

aux.drawText(text)
aux.showPage()
aux.save()