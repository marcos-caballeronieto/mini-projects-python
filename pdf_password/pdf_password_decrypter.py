import PyPDF2

filename = "Encrypted sample-local-pdf.pdf"

pdf_reader = PyPDF2.PdfReader(filename)
pdf_writer = PyPDF2.PdfWriter()

password = input("Write your password to decrypt your pdf")

if pdf_reader.is_encrypted:
    pdf_reader.decrypt(password)

for page in pdf_reader.pages:
    pdf_writer.add_page(page)

new_filename = "Decrypted" + filename
with open(new_filename, "wb") as f:
    pdf_writer.write(f)