from django.http import HttpResponse
from django.shortcuts import render, redirect
from pptx import Presentation
from docx import Document
from .gpt_service import get_summary_from_gpt  # Place gpt_service.py in the my_app directory

# Home view to display the welcome message and link to the upload page
def home(request):
    return render(request, 'home.html')

# Combined upload view for handling both PowerPoint and Word uploads
def upload(request):
    if request.method == 'POST':
        ppt_file = request.FILES.get('ppt_file')
        word_file = request.FILES.get('word_file')

        # Handle PowerPoint upload
        if ppt_file and ppt_file.name.endswith('.pptx'):
            prs = Presentation(ppt_file)
            slides_text = []
            for slide in prs.slides:
                for shape in slide.shapes:
                    if hasattr(shape, "text"):
                        slides_text.append(shape.text)
            summarized_content = get_summary_from_gpt(' '.join(slides_text))
            return render(request, 'summaryppt.html', {'original_content': slides_text, 'summarized_content': summarized_content})

        # Handle Word upload
        elif word_file and word_file.name.endswith('.docx'):
            document = Document(word_file)
            doc_text = []
            for para in document.paragraphs:
                doc_text.append(para.text)
            # Combine all the text into a single string
            full_text = '\n'.join(doc_text)
            # Get the summarized content
            summary = get_summary_from_gpt(full_text)
            return render(request, 'summaryword.html', {'summary': summary})
            
    return render(request, 'upload.html')