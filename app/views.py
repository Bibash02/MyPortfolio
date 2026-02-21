from django.shortcuts import redirect, render
from .models import ContactMessage
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def portfolio(request):
    return render(request, 'portfolio.html')

def contact(request):
    if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            budget = request.POST.get('budget')
            message = request.POST.get('message')


            ContactMessage.objects.create(
                first_name = first_name,
                last_name = last_name,
                email = email,
                subject = subject,
                budget = budget,
                message = message,
            )

            # send email to the gmail
            full_message = f"""
            New Contact Message from Portfolio

            Name: {first_name} {last_name}
            Email: {email}
            Subject: {subject}
            Budget: {budget}

            Message:
            {message}
            """

            send_mail(
                 subject=f"New Contact Message: {subject}",
                 message=full_message,
                 from_email=settings.EMAIL_HOST_USER,
                 recipient_list=["bayalkotibibash@gmail.com"]
            )
            return redirect('contact')
    
    return render(request, 'contact.html')

def projects(request):
    return render(request, 'projects.html')