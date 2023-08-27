import requests
from lfg_project.celery import app
from .models import Proposal

@app.task
def process_proposal(proposal_id):
    proposal = Proposal.objects.get(id=proposal_id)
    url = 'https://loan-processor.digitalsys.com.br/api/v1/loan'
    data = {
        'name': proposal.name,
        'document': proposal.cpf,
    }
    response = requests.post(url, json=data)
    result = response.json()
    if result['approved']:
        proposal.status = 'human'
    else:
        proposal.status = 'denied'
    proposal.save()
