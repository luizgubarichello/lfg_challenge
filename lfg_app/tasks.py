from celery import shared_task
import requests
from .models import Proposal


@shared_task
def process_proposal(proposal_id):
    proposal = Proposal.objects.get(id=proposal_id)
    data = {}
    for field_value in proposal.fields.all():
        data[field_value.field.name] = field_value.value
    response = requests.post('https://loan-processor.digitalsys.com.br/api/v1/loan', data=data)
    if response.status_code == 200:
        result = response.json()
        if result['approved']:
            proposal.status = 'human'
        else:
            proposal.status = 'denied'
        proposal.save()
    else:
        print(f'Erro ao chamar a API de Análise de Crédito: {response.status_code}')
