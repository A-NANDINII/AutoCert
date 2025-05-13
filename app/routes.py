from flask import render_template, request, send_from_directory, flash, redirect, url_for
from app import app
import os
from werkzeug.utils import secure_filename
from .certificate_generator import generate_certificates

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'csv'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    if 'template' not in request.files or 'csv' not in request.files:
        flash('Both files are required!')
        return redirect(url_for('index'))
    
    template = request.files['template']
    csv_file = request.files['csv']
    
    if template.filename == '' or csv_file.filename == '':
        flash('No selected files')
        return redirect(url_for('index'))
    
    if template and allowed_file(template.filename) and csv_file and allowed_file(csv_file.filename):
        template_filename = secure_filename(template.filename)
        csv_filename = secure_filename(csv_file.filename)
        
        template_path = os.path.join(app.config['UPLOAD_FOLDER'], template_filename)
        csv_path = os.path.join(app.config['UPLOAD_FOLDER'], csv_filename)
        
        template.save(template_path)
        csv_file.save(csv_path)
        
        output_filename = generate_certificates(template_path, csv_path)
        
        return send_from_directory(
            app.config['UPLOAD_FOLDER'],
            output_filename,
            as_attachment=True,
            download_name='generated_certificates.pdf'
        )
    
    flash('Invalid file types. Allowed: PNG, JPG for template and CSV for data')
    return redirect(url_for('index'))