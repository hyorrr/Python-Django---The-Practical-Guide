from django.urls import path
from . import views

urlpatterns = [
    # path("january", views.january),
    # path("feburary", views.feburary),
    # path("march", views.march)
    
    # Path Converts
    # Dynamic Path Segements
    # 순서에 주의하자 pay attention to order
    path("", views.index), # trigger /challenges/
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge") 
]

