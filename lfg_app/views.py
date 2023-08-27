from rest_framework import generics
from .models import Proposal
from .serializers import ProposalSerializer
from .tasks import process_proposal
from django.shortcuts import render


def home(request):
    return render(request, "lfg_app/home.html")


class ProposalCreateView(generics.ListCreateAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer

    def perform_create(self, serializer):
        proposal = serializer.save()
        process_proposal.delay(proposal.id)
