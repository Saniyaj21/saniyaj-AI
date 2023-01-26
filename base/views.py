from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import openai
from . import keys





# Create your views here.

def home(request):
    
    return render(request, 'home.html')
def blogs(request):
    answer = "Saniyaj will answer all of your questions 😎"
    context = {'answer':answer}
    if request.method == "POST":
        ask = request.POST.get('question')
        
        

        # Set the API key
        openai.api_key = keys.OPENAI_API_KEY

        

        # Use the Completion API to generate text
        completion = openai.Completion.create(
            engine="text-davinci-002",
            prompt=ask,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        answer = (completion.choices[0].text)
        context = {'answer':answer, 'ask':ask}




    
    return render(request, 'blogs.html',context)
def courses(request):
    
    return render(request, 'courses.html')
