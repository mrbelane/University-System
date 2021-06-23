from django import forms


class editForm(forms.Form):
    first_name = forms.CharField(label='first_name', max_length=100)
    last_name = forms.CharField(label='last_name', max_length=100)
    major = forms.IntegerField(label='major')
    grade = forms.IntegerField(label='grade')


class loginForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', max_length=100)
