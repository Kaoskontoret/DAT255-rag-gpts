import requests
from bs4 import BeautifulSoup
from fpdf import FPDF
import os

urls = [
    "https://www.fjord1.no/Om-Fjord1",
    "https://www.fjord1.no/Om-Fjord1/Forretningsomraada-vaare/Ferjer",
    "https://www.fjord1.no/Om-Fjord1/Visjon-verdiar-og-etikk",
    "https://www.fjord1.no/Om-Fjord1/Historia-vaar",
]

os.makedirs("fjord1_pdfs", exist_ok=True)

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    page_text = soup.get_text(separator=" ", strip=True)

    filename = url.split("/")[-1] or "index"
    pdf_path = f"fjord1_pdfs/{filename}.pdf"

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in page_text.splitlines():
        pdf.multi_cell(0, 10, line)

    pdf.output(pdf_path)
    print(f"Saved {pdf_path}")

print("All PDFs saved in 'fjord1_pdfs/' folder.")
