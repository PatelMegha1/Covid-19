from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CovidForm
from datetime import datetime 


# Create your views here.
def form(request, *args, **kwargs):
    if request.method == 'POST':
        form = CovidForm(request.POST)
        if form.is_valid():
            form.save()
            if form.cleaned_data['question1'] == 'YES' or form.cleaned_data['question2'] == 'YES' or form.cleaned_data['question3'] == 'YES' or form.cleaned_data['question4'] == 'YES':
                if  form.cleaned_data['question1'] == 'YES':
                    alert = "Please consult your family physician, inform manager, or proceed to the assessment center (London Oakridge Arena – 825 Valetta Street – east of Hyde park) "
                    print(alert)
                    return render(request, 'error.html',{'alerts':alert})
                else:
                    # if form.cleaned_data['question2'] == 'YES' or form.cleaned_data['question3'] == 'YES' or form.cleaned_data['question4'] == 'YES':
                    alert = "Please DO NOT come to KGK, self-isolate, inform your manager, family physician and infectious disease control team at the Middlesex-London Health Unit 519-663-5317."
                    print(alert)
                    return render(request, 'error.html',{'alerts':alert})
            else:
                print("Success condition")
                return redirect('success/')
    else:
        form = CovidForm()
        print("GET")
    return render(request, 'form.html', {'form':form})




def success(request, *args, **kwargs):
    return render(request, 'success.html')
