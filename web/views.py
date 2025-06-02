from django.shortcuts import render, get_object_or_404
from .models import Member

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def member_list(request):
    members = Member.objects.all()
    return render(request, 'member_list.html', {'members': members})

def member_detail(request, id):
    member = get_object_or_404(Member, id=id)
    return render(request, 'member_detail.html', {'member': member})
