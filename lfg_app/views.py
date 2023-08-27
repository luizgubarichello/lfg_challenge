from rest_framework import generics, status
from rest_framework.response import Response
from .models import ProposalField, Proposal, ProposalFieldValue
from .serializers import ProposalFieldSerializer, ProposalSerializer
from .tasks import process_proposal
from django.shortcuts import render

def home(request):
    return render(request, "lfg_app/home.html")


class ProposalFieldListCreateView(generics.ListAPIView):
    queryset = ProposalField.objects.all() 
    serializer_class = ProposalFieldSerializer 


class ProposalListCreateView(generics.ListCreateAPIView):
    queryset = Proposal.objects.all() 
    serializer_class = ProposalSerializer 

    def perform_create(self, serializer):
        proposal = serializer.save() 
        process_proposal.delay(proposal.id)


class ProposalRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer

    def update(self, request, *args, **kwargs):
        proposal = self.get_object()
        if proposal.status in ('approved', 'denied'): 
            return Response({'detail': 'Proposta já possui um status final e não pode ser alterada.'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)
