from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage
from personal_portfolio.settings import EMAIL_HOST_USER, CONTACT_EMAIL
from .forms import ContactForm
from .models import Project, Expertise, Certificate

# Create your views here.
def home(request):
    expertises = Expertise.objects.all()
    return render(request, 'portfolio/home.html', {'expertises':expertises})

def portfolio(request):
    projects = Project.objects.all()
    certificates = Certificate.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects': projects, 'certificates': certificates})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            send_mail(
                subject, 
                f"Message from {name} ({email}):\n\n{message}",
                EMAIL_HOST_USER,
                [CONTACT_EMAIL],
                fail_silently=False,
            )
            return JsonResponse({'message': 'Message sent successfully!'}, status=200)
        else:
            JsonResponse({'error': 'Invalid form submission.'}, status=400)
    else:
        form = ContactForm()
        return JsonResponse({'error': 'Invalid request method.'}, status=400)
