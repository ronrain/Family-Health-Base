from django.shortcuts import render, redirect
from .models import Member

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def member_index(request):
  members = Member.objects.all()
  return render(request, 'members/index.html', { 'members': members })

def member_detail(request, cat_id):
  member = Member.objects.get(id=cat_id)
  return render(request, 'members/detail.html', { 'member': member })