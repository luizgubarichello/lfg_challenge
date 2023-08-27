from django.db import models

class Proposal(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendente'),
        ('approved', 'Aprovada'),
        ('denied', 'Negada'),
        ('human', 'Humano'),
    ]
    name = models.CharField(max_length=100, verbose_name='Nome')
    email = models.EmailField(max_length=100, verbose_name='E-mail')
    cpf = models.CharField(max_length=11, verbose_name='CPF')
    income = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Renda')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor Solicitado')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name='Status')

    def __str__(self):
        return f"Proposta {self.id}: {self.status}"
