from django.contrib.staticfiles.views import serve
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django_mkdocs import settings
import os


def index_view(request):
    return redirect(reverse('docs'))


@login_required
def serve_docs(request, path):
    docs_path = os.path.join(settings.DOCS_DIR, path)
 
    if os.path.isdir(docs_path):
       path = os.path.join(path, 'index.html')
    
    path = os.path.join(settings.DOCS_STATIC_NAMESPACE, path)
    
    return serve(request, path, insecure=True)

