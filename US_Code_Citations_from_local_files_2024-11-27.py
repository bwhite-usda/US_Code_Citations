import PyPDF2
import re
import pandas as pd

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

# Function to find US Code citations in text
def find_us_code_citations(text):
    pattern = r'\b(?:\d{1,2}\sU\.S\.C\.|\d{1,2}\sUSC|\d{1,2}\sU\.S\.\sCode|\d{1,2}\sU\.S\.\sC\.|\d{1,2}\sUS\sCode|chapter\s\d+\sof\stitle\s\d+,\sUnited\sStates\sCode|\d+\(\w+\)\sof\stitle\s\d+,\sUnited\sStates\sCode)\s?' r'[\d\w\(\)\-\—]*\b'
    return re.findall(pattern, text)

# Paths of the local PDFs
pdf_paths = [
    r"C:\Users\basil.white\Python\00-Preface-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\01-OSEC-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\02-OHS-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\03-OPPE-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\04-DA-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\05-OC-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\06-OCE-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\07-OHA-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\10a-OCFO-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\10b-WCF-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\11-OCR-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\12-AgBF-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\13-HMM-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\15-OIG-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\16-OGC-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\17-OE-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\18-ERS-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\19-NASS-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\20-ARS-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\21-NIFA-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\22-APHIS-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\23-AMS-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\24-FSIS-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\25-FBC-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\26-FSA-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\27-RMA-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\28-NRCS-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\29-CCC-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\29a-FS-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\30-RD-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\31-RHS-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\32-RBCS-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\33-RUS-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\34-FNS-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\35-FAS-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\36-General-Provisions-2025-ExNotes.pdf",
    r"C:\Users\basil.white\Python\38-Congressional-Directives-2025-ExNotes.pdf",
]

# List to hold the results
data = []

# Extract and search each PDF (skip download since files are local)
for pdf_filename in pdf_paths:
    text = extract_text_from_pdf(pdf_filename)
    citations = find_us_code_citations(text)
    for citation in citations:
        data.append({"PDF": pdf_filename, "US Code Citation": citation})

# Create a DataFrame and save to Excel
df = pd.DataFrame(data)
df.to_excel("US_Code_Citations.xlsx", index=False)


