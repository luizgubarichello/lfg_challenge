from django.urls import path
from .views import ProposalFieldListCreateView, ProposalListCreateView, ProposalRetrieveUpdateView, home

urlpatterns = [
    path('fields/', ProposalFieldListCreateView.as_view(), name='proposal-field-list-create'),
    path('', home, name='main_home'),
    path('proposals/', ProposalListCreateView.as_view(), name='proposal-list-create'),
    path('proposals/<int:pk>/', ProposalRetrieveUpdateView.as_view(), name='proposal-retrieve-update'),
]