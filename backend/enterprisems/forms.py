from django import forms
from validate_cnpj import validate_cnpj
from users.models import User
from enterprisems.models import Company, Department


class LoginForm(forms.Form):
    """Formulário para coletar credenciais de login"""

    email = forms.EmailField(
        label="Email", widget=forms.EmailInput(attrs={"placeholder": "Email"})
    )

    password = (
        forms.CharField(
            label="Senha", attrs={"placeholder": "Senha", "class": "form-control"}
        ),
    )


class CreateCompany(forms.ModelForm):
    """Formulário para criar uma empresa"""

    class Meta:
        model = Company
        fields = ["name", "cnpj", "address", "phone"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"placeholder": "Nome"})
        self.fields["cnpj"].widget.attrs.update({"placeholder": "CNPJ"})
        self.fields["address"].widget.attrs.update({"placeholder": "Endereço"})
        self.fields["phone"].widget.attrs.update({"placeholder": "Telefone"})

    def clean_cnpj(self):
        cnpj = self.cleaned_data["cnpj"]
        if not validate_cnpj(cnpj):
            raise forms.ValidationError("CNPJ inválido.")
        return cnpj

    def save(self, commit=True):
        company = super().save(commit=False)
        company.save()
        return company


class CreateDepartment(forms.ModelForm):
    """Formulário para criar um departamento"""

    class Meta:
        model = Department
        fields = ["name", "cnpj"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"placeholder": "Nome"})
        self.fields["cnpj"].widget.attrs.update({"placeholder": "CNPJ"})

    def clean_cnpj(self):
        cnpj = self.cleaned_data["cnpj"]
        if not validate_cnpj(cnpj):
            raise forms.ValidationError("CNPJ inválido.")
        return cnpj

    def save(self, commit=True):
        department = super().save(commit=False)
        department.save()
        return department
