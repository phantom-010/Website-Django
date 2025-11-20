from django import forms
from .models import *


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['contract_number', 'contract_date', 'partner', 'subject']