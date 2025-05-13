import pandas as pd
from fpdf import FPDF
import os
from datetime import datetime
from PIL import Image

def generate_certificates(template_path, csv_path):
    # Verify template dimensions
    with Image.open(template_path) as img:
        width, height = img.size
    
    # Read participant data
    df = pd.read_csv(csv_path)
    
    pdf = FPDF(unit="pt", format=[width, height])
    
    for _, row in df.iterrows():
        pdf.add_page()
        pdf.image(template_path, x=0, y=0, w=width, h=height)
        
        # Add participant name (centered)
        pdf.set_font("Arial", "B", 48)
        pdf.set_xy(0, height/2 - 50)
        pdf.cell(width, 0, row['Name'], 0, 0, 'C')
        
        # Add event details
        pdf.set_font("Arial", "", 24)
        pdf.set_xy(0, height/2 + 20)
        pdf.cell(width, 0, f"for participating in {row['Event']}", 0, 0, 'C')
        
        # Add date
        pdf.set_font("Arial", "I", 18)
        pdf.set_xy(0, height - 100)
        pdf.cell(width, 0, datetime.now().strftime("%B %d, %Y"), 0, 0, 'C')
    
    output_filename = f"certificates_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    output_path = os.path.join(os.path.dirname(template_path), output_filename)
    pdf.output(output_path)
    
    return output_filename