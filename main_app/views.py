from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView
from .models import Member, Appointment
from .forms import AppointmentForm

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def member_index(request):
  members = Member.objects.all()
  return render(request, 'members/index.html', { 'members': members })

def member_detail(request, member_id):
  member = Member.objects.get(id=member_id)
  appointment_form = AppointmentForm()
  return render(request, 'members/detail.html', { 'member': member, 'appointment_form': appointment_form })

class MemberCreate(CreateView):
  model = Member
  fields = '__all__'
  success_url = '/members/'

class MemberUpdate(UpdateView):
  model = Member
  fields = ['gender', 'height', 'weight', 'medical_history', 'update_date']

class MemberDelete(DeleteView):
  model = Member
  success_url = '/members/'

def add_appointment(request, member_id):
  form = AppointmentForm(request.POST)
  if form.is_valid():
    new_appointment = form.save(commit=False)
    new_appointment.member_id = member_id
    new_appointment.save()
  return redirect('member-detail', member_id=member_id)

class AppointmentDetail (DetailView):
  model = Appointment

class AppointmentUpdate(UpdateView):
  model = Appointment
  fields = ['date', 'appointment_type', 'diagnosis', 'treatment', 'follow_up']

class AppointmentDelete(DeleteView):
  model = Appointment
  success_url = '/members/member_id'