from django.shortcuts import render
from .models import contact

def home(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact.objects.create(
            name=name,
            email=email,
            message=message
        )

    return render(request, 'index.html')