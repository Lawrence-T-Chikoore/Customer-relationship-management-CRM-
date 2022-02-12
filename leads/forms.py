from django import forms


class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name =forms.CharField()
    age = forms.IntegerField(max_value=0)