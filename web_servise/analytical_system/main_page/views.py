from django.shortcuts import render

# Create your views here.

def main_page_render(request):
    return render(request, 'main_page/main.html')

def about_project_render(request):
    return render(request, 'about_project/about_project.html')

def analysis_render(request):
    return render(request, 'analysis/analysis.html')
