import PyPDF2

filename = "sample-local-pdf.pdf"

pdf_reader = PyPDF2.PdfReader(filename)
pdf_writer = PyPDF2.PdfWriter()

for page in pdf_reader.pages:
    pdf_writer.add_page(page)

password = input("Write your password")
confirmation = input("Write your password again")
#For the encrypted sample pdf the password is "1234"

if password == confirmation:
    pdf_writer.encrypt(password)
    new_filename = "Encrypted " + filename
    with open(new_filename, "wb") as f:
        pdf_writer.write(f)