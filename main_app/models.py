from django.db import models
from django.urls import reverse

GENDER = (
  ('M', 'Male'),
  ('F', 'Female'),
  ('N', 'Non-Binary'),
  ('P', 'Prefer Not to Say')
)

class Member(models.Model):
  name = models.CharField(max_length=100)
  birth_date = models.DateField('Birth date')
  gender = models.CharField(
    max_length=1,
    choices=GENDER
  )
  height = models.IntegerField()
  weight = models.IntegerField()
  medical_history = models.TextField(max_length=250)
  update_date = models.DateField('Update date')

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('member-detail', kwargs={'member_id': self.id})