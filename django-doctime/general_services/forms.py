from django import forms
from general_services.models import PescribedMedicine


class PescribedMedicineForm(forms.ModelForm):

    class Meta:
        model = PescribedMedicine
        fields = ['comments', 'medicine', 'test']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['medicine'].widget.attrs.update({'class': 'form-control',})
        self.fields['test'].widget.attrs.update({'class': 'form-control',})
        self.fields['comments'].widget.attrs.update({'class': 'form-control',})