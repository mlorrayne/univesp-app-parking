from django import forms

from .models import Customer


class CustomerForm(forms.ModelForm):
    first_name = forms.CharField(
        label="Nome",
        error_messages={"max_length": "Nome não pode ter mais de 30 caracteres"}
        )
    last_name = forms.CharField(
        label="Sobrenome",
        error_messages={"max_length": "Sobrenome não pode ter mais de 50 caracteres"}
        )
    number_plate = forms.CharField(label="Placa")
    area_code = forms.RegexField(
        label="DDD",
        regex=r"^\+?1?[0-9]{2}$",
        error_messages={"invalid": "Número de DDD Inválido"}
        )
    phone_number = forms.RegexField(
        label="Telefone",
        regex=r"^\+?1?[0-9]{8,15}$",
        error_messages={"invalid": "Número de Telefone Inválido"}
        )
    city = forms.CharField(label="Cidade")

    class Meta:
        model = Customer
        fields = (
            "first_name",
            "last_name",
            "number_plate",
            "area_code",
            "phone_number",
            "city",
            "departure_time"    
        )