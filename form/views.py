import csv, requests


from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.core.mail import send_mail
from .forms import CovidForm
from datetime import datetime 
from .models import CovidModel


email_recipients =['mpatel@dsstoronto.com','ndesai@dsstoronto.com']
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
                    send_mail('Covid Alert from Front Door',
                    'Person reported with potential to spread Corona Virus, and is refused to enter the Building and requested to \n "' + alert +'"',
                    'todaycovid@gmail.com',
                    email_recipients,
                    fail_silently = False)
                    return render(request, 'error.html',{'alerts':alert})
                else:
                    # if form.cleaned_data['question2'] == 'YES' or form.cleaned_data['question3'] == 'YES' or form.cleaned_data['question4'] == 'YES':
                    alert = "Please DO NOT come to KGK, self-isolate, inform your manager, family physician and infectious disease control team at the Middlesex-London Health Unit 519-663-5317."
                    print(alert)
                    send_mail('Covid Alert from Front Door',
                    'Person reported with potential to spread Corona Virus, and is refused to enter the Building and requested to \n "' + alert +'"',
                    'todaycovid@gmail.com',
                    email_recipients,
                    fail_silently = False)
                    return render(request, 'error.html',{'alerts':alert})
            else:
                print("Success condition")
                return render(request, 'success.html')
    else:
        form = CovidForm()
        print("GET")
    return render(request, 'form.html', {'form':form})



def download_csv(request):
    items = CovidModel.objects.all()

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Covid_Survey_report_on_' + str(datetime.now())  + '.csv"'

    writer = csv.writer(response, delimiter = ',')
    writer.writerow(['Name','Question1','Question2', 'Question3', 'Question4', 'Date'])
    for obj in items:
        writer.writerow([obj.Name, obj.question1, obj.question2, obj.question3, obj.question4, obj.date])

    return response

def email(request):
    send_mail('"Covid_Survey_report_on_' + str(datetime.now())  + '.csv"',
     "Please find the report in the link below  \n http://192.168.2.200:8000/download-csv " ,
     'todaycovid@gmail.com',
     email_recipients,
     fail_silently = False)
    return HttpResponse("Email Sent")