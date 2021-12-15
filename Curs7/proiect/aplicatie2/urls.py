from django.urls import path
from aplicatie2 import views

app_name = 'aplicatie2'

urlpatterns =[
    path('new_timesheet', views.newPontaj, name='pontaj'),
    path('stop_timesheet', views.stopTimesheet, name='oprire_pontaj'),
]