from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widge=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widge.attrs={
            'class':'form-control'
        }
        self.fields['email'].widge.attrs={
            'class':'form-control'
        }
        self.fields['password'].widge.attrs={
            'class':'form-control'
        }