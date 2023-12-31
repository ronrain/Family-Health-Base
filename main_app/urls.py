from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('members/', views.member_index, name='member-index'),
  path('members/<int:member_id>/', views.member_detail, name='member-detail'), 
  path('members/create/', views.MemberCreate.as_view(), name='member-create'),
  path('members/<int:pk>/update/', views.MemberUpdate.as_view(), name='member-update'),
  path('members/<int:pk>/delete/', views.MemberDelete.as_view(), name='member-delete'),
  path('members/<int:member_id>/add-appointment/', views.add_appointment, name='add-appointment'),
  path('appointments/<int:pk>/', views.AppointmentDetail.as_view(), name='appointment-detail'),
  path('appointments/<int:pk>/update/', views.AppointmentUpdate.as_view(), name='appointment-update'),
  path('appointments/<int:pk>/delete/', views.AppointmentDelete.as_view(), name='appointment-delete'),
  path('accounts/signup/', views.signup, name='signup'),
]
