from django.urls import path
from . import views

urlpatterns = [
    # path("january", views.january),
    # path("feburary", views.feburary),
    # path("march", views.march)
    
    # Path Converts
    # Dynamic Path Segements
    path("", views.index), # trigger /challenges/
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge") 
]

