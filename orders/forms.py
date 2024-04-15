from django import forms
from .models import Customer

class CustomerCreateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'address',
        'postal_code', 'city']