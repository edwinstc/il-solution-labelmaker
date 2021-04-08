import streamlit as st
from fpdf import FPDF
import pandas as pd
import base64

st.title('Sample Label Maker')
Solute = st.text_input('Enter the solute of the mixture')
Solvent = st.text_input('Enter the solvent used')
Date = st.text_input('Enter date of sample prep in format yyyymmdd')
Owner = st.text_input('Enter the name of the sample owner')
Comments = st.text_input('Enter any additional comments. Limit of 15 characters')
CS_composition = st.file_uploader('File uploader',type='csv')
show_file = st.empty()

def Make_pdf():
    pdf = FPDF('L','in',(0.7,1.4))
    pdf.set_auto_page_break(0)
    pdf.set_margins(0.1,0.1,0.3)
    pdf.set_font('Helvetica','',6.5)
    return pdf

def Print_labels(data,pdf):
    for i in range(0,len(data)):
        pdf.add_page()
        text = (f'Name: {Solute}/{Solvent}\nConc: {str(concentrations[i])} m\nDate: {Date}\nOwner: {Owner}\nCom:{Comments}')
        pdf.multi_cell(1.25,0.1,txt=text)
    pdfname = str(f'Labels_{Solute}_{Date}.pdf')
    pdf.output(pdfname)
    return pdfname

def st_display_pdf(pdf_file):  
    with open(pdf_file,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
    st.markdown(pdf_display, unsafe_allow_html=True)

if not CS_composition:
    ''
else:
    data = pd.read_csv(CS_composition)
    concentrations = data["Actual"]
    doc = Make_pdf()
    pdfname = Print_labels(data,doc)

if st.button('Make labels'):
    st.text(Solute)
    st_display_pdf(pdfname)