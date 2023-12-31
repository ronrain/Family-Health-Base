from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

OPTIONS = (
  ('Yes', 'Yes'),
  ('No', 'No')
)

GENDER = (
  ('Male', 'Male'),
  ('Female', 'Female'),
  ('Non-Binary', 'Non-Binary'),
  ('Prefer Not to Say', 'Prefer Not to Say')
)

class Member(models.Model):
  name = models.CharField(max_length=100)
  birth_date = models.DateField('Birth Date')
  gender = models.CharField(
    max_length=100,
    choices=GENDER
  )
  height = models.IntegerField()
  weight = models.IntegerField()
  medical_history = models.TextField(max_length=250)
  update_date = models.DateField('Update Date')
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('member-detail', kwargs={'member_id': self.id})
  
class Appointment(models.Model):
  date = models.DateField('Appointment Date')
  appointment_type = models.CharField(max_length=100)
  diagnosis = models.CharField(
    max_length=100, 
    null=True, 
    blank=True
  )
  treatment = models.TextField(
    max_length=250, 
    null=True, 
    blank=True
  )
  follow_up = models.CharField(
    max_length=100,
    choices=OPTIONS,
    default=OPTIONS[1][0]  
  )
  follow_up_date = models.DateField(null=True, blank=True)

  member = models.ForeignKey(Member, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.appointment_type} on {self.date}"
  
  class Meta:
    ordering = ['-date']