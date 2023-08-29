from django.http import HttpResponse
from django.shortcuts import render, redirect
from pptx import Presentation
from .gpt_service import get_summary_from_gpt  # Place gpt_service.py in the my_app directory

def upload_file(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        if file and file.name.endswith('.pptx'):
            prs = Presentation(file)
            slides_text = []
            for slide in prs.slides:
                for shape in slide.shapes:
                    if hasattr(shape, "text"):
                        slides_text.append(shape.text)
            summarized_content = get_summary_from_gpt(' '.join(slides_text))
            return render(request, 'results.html', {'original_content': slides_text, 'summarized_content': summarized_content})
    return render(request, 'upload.html')