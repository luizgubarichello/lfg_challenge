from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main_home'),
    path('proposals/', views.ProposalCreateView.as_view(), name='proposal-create'),
]
