from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def contact_email(request):
    context = {
    }
    if request.method == 'POST':
        name = request.POST.get('name', '')  # Assign 'name' from POST data
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')


        if name and email and message:
            full_message = f'Name: {name}\nEmail: {email}\n\n{message}'
            send_mail(
                'Contact Request - MTF2023',
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                ['mcet.mtf@gmail.com'],
                fail_silently=False,
            )
            context['success'] = 'Your message has been sent. Thank you for contacting us!'
        else:
            context['error'] = 'Please fill in all required fields.'

    return render(request, 'userreg/index.html',context)






def contact_email2(request):
    context = {
    }
    if request.method == 'POST':
        name = request.POST.get('name', '')  # Assign 'name' from POST data
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')


        if name and email and message:
            full_message = f'Name: {name}\nEmail: {email}\n\n{message}'
            send_mail(
                'Contact Request - MTF2023',
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                ['mcet.mtf@gmail.com'],
                fail_silently=False,
            )
            context['success'] = 'Your message has been sent. Thank you for contacting us!'
        else:
            context['error'] = 'Please fill in all required fields.'

    return render(request, 'userreg/pt.html',context)


