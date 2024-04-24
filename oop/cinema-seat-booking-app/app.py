import random, string 
from fpdf import FPDF
t_id = "".join([random.choice(string.ascii_uppercase) for i in range (10)])

print(t_id)


"""Creates a PDF Ticket"""
pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()
            
# Create the ticket title 
pdf.set_font('Times', style='B', size=24)
pdf.cell(w=0, h=80, txt='CPL Digital Cinema Ticket', border=1, ln=1, align='C')
            
# create the name cell
pdf.set_font('Times', style='B', size=14)
pdf.cell(w=100, h=25, txt='Name', border=1)
pdf.set_font('Times', style='B', size=14)
pdf.cell(w=0, h=25, txt='Elvis', border=1, ln=1)

pdf.output('sample pdf')