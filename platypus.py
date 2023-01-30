import os

from reportlab.platypus import Paragraph
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

class MeuParagraphStyle (ParagraphStyle):
   def __init__ (self):
      super().__init__(self, fontSize = 18,
                       font= 'Helvetica',
                       textColor = 'Grey'
                       )
      self.defaults['fontName'] = 'Helvetica'
      self.defaults['fontSize'] = 18
      self.defaults['textColor'] = 'Grey'

follaEstilo = getSampleStyleSheet()

operacions =  []

cabeceira = follaEstilo ['Heading4']
cabeceira.pageBreakBefore = 1
cabeceira.keepWithNext = 0
cabeceira.backColor = colors.cornsilk

paragrafo = Paragraph ("Cabeceira do documento", cabeceira)
operacions.append (paragrafo)

cadea = """Texto de contido do paragrafo que imos repetir unha cuantas veces""" * 500
textoNormal = follaEstilo['BodyText']
parrafo2 = Paragraph(cadea*100, textoNormal)

operacions.append (Spacer(0,20))

ficheiro_imaxe = "/home/dam2a/Descargas/pinguino.png"
imaxe = Image(os.path.realpath(ficheiro_imaxe), width = 225, height = 225)
operacions.append(imaxe)

paragrafo3 = Paragraph(cadea*5, MeuParagraphStyle())
operacions.append(paragrafo3)

documento = SimpleDocTemplate("exemploPatypus.pdf", pagesize = A4, showBoundary = 1)
documento.build(operacions)