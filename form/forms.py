from django import forms
from django.core.validators import MaxLengthValidator

from form.models import Person


class PersonForm(forms.Form):
    first = forms.CharField(initial='hello', label='input1', help_text='help_text')
    second = forms.CharField(validators=[MaxLengthValidator(10)])

    def save(self):
        print(self.cleaned_data)
        pass


class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
