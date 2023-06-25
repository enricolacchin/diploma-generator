import os
import pandas as pd
from reportlab.pdfgen import canvas
from PyPDF3 import PdfFileReader, PdfFileWriter
from datetime import datetime
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from io import BytesIO

# Register the fonts
pdfmetrics.registerFont(TTFont('EdwardianScriptITC', 'font/EdwardianScriptITC.ttf'))
pdfmetrics.registerFont(TTFont('Bahnschrift', 'font/Bahnschrift.ttf'))

# Read the Excel file with Pandas
df = pd.read_excel('user_list.xlsx')

# Make sure Diplomas folder exists
if not os.path.exists('Diplomas'):
    os.makedirs('Diplomas')

for index, row in df.iterrows():
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=(400, 280))  # Adjusted size of your PDF

    # Add the name to the PDF
    name = row['name']
    can.setFont('EdwardianScriptITC', 32)
    name_width = pdfmetrics.stringWidth(name, 'EdwardianScriptITC', 32)
    can.drawString((400 - name_width) / 2, 128, name)  # Replace 400 with your page width

    # Add the current date
    current_date = datetime.now().strftime("%d-%m-%Y")
    can.setFont('Bahnschrift', 7)
    can.drawString(111, 280 - 235, current_date)  # Adjusted position for date

    can.save()

    # Move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)

    # Read your existing PDF
    existing_pdf = PdfFileReader(open("diploma.pdf", "rb"))
    output = PdfFileWriter()

    # Add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.pages[0]
    page.mergePage(new_pdf.pages[0])
    output.addPage(page)

    # Finally, write "output" to a real file
    outputStream = open(f"Diplomas/diploma_{row['name']}.pdf", "wb")
    output.write(outputStream)
    outputStream.close()