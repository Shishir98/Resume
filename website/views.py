import os
from django.http import FileResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def download_resume(request):
    # Check if the uploaded file is a PDF
    # Use os.path.join for creating file paths
    pdf_file_path = os.path.join('static', 'website', 'documents', 'Shishir Saxena - Resume.docx.pdf')

    print(f"PATH: {os.getcwd()}")
    # Provide a custom name for the downloaded file (optional)
    custom_file_name = 'resume.pdf'

    # Make sure the file exists before attempting to serve it
    if os.path.exists(pdf_file_path):
        return FileResponse(open(pdf_file_path, 'rb'), as_attachment=True, filename=custom_file_name)
    else:
        # Handle the case where the file doesn't exist
        return render(request, 'file_not_found.html', {})
