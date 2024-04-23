from django import forms


from helper.models import Helper,Customer


class HelperForm(forms.ModelForm):
    class Meta:
        model=Helper
        exclude=('customer',)

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.Select(attrs={'class':'form-select'}),
            'skills':forms.Textarea(attrs={'class':'form-control','rows':3}),
            'age':forms.NumberInput(attrs={'class':'form-control'}),
            
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields='__all__'

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control','rows':3}),
            'phone_number':forms.TextInput(attrs={'class':'form-control'}),
           
            
        }

    