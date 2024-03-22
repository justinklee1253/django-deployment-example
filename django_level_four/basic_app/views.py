from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict = {'text': 'hello world', 'number': 100} #pass data to the template
    #transfer data from view to template, allow template to display dynamic content from database/userinput
    return render(request, 'basic_app/index.html', context_dict) #render usually used to load a template and a context

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative_url_templates.html')
