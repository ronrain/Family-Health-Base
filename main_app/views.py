from django.shortcuts import render, redirect
from django.urls import reverse
from datetime import date
from django.contrib.auth import login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView
from .models import Member, Appointment
from .forms import AppointmentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def member_index(request):
  members = Member.objects.filter(user=request.user)
  return render(request, 'members/index.html', { 'members': members })

@login_required
def member_detail(request, member_id):
  member = Member.objects.get(id=member_id)
  appointment_form = AppointmentForm()
  today = date.today()
  has_appointment_today = Appointment.objects.filter(member=member, date=today).exists()
  return render(request, 'members/detail.html', { 'member': member, 'appointment_form': appointment_form, 'has_appointment_today': has_appointment_today })

class MemberCreate(LoginRequiredMixin, CreateView):
  model = Member
  fields = ['name', 'birth_date', 'gender', 'height', 'weight', 'medical_history', 'update_date']
  success_url = '/members/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class MemberUpdate(LoginRequiredMixin, UpdateView):
  model = Member
  fields = ['gender', 'height', 'weight', 'medical_history', 'update_date']

class MemberDelete(LoginRequiredMixin, DeleteView):
  model = Member
  success_url = '/members/'

@login_required
def add_appointment(request, member_id):
  form = AppointmentForm(request.POST)
  if form.is_valid():
    new_appointment = form.save(commit=False)
    new_appointment.member_id = member_id
    new_appointment.save()
  return redirect('member-detail', member_id=member_id)

class AppointmentDetail(LoginRequiredMixin, DetailView):
  model = Appointment

class AppointmentUpdate(LoginRequiredMixin, UpdateView):
  model = Appointment
  fields = ['date', 'appointment_type', 'diagnosis', 'treatment', 'follow_up', 'follow_up_date']

  def get_success_url(self):
    return reverse('appointment-detail', kwargs={'pk': self.object.pk})


class AppointmentDelete(LoginRequiredMixin, DeleteView):
  model = Appointment

  def get_success_url(self):
    member_id = self.object.member.id
    return reverse('member-detail', kwargs={'member_id': member_id})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('member-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
