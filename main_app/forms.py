from django.forms import ModelForm
from .models import Appointment

class AppointmentForm(ModelForm):
  class Meta:
    model = Appointment
    fields = ['date', 'visit_type', 'diagnosis', 'treatment', 'follow_up']