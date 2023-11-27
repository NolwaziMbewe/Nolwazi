from django import forms
from django.forms import formset_factory
from django.forms.widgets import TextInput

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20,label="",widget=TextInput(attrs={'placeholder':'Enter Username','class':'form-control'}))
    password = forms.CharField(max_length=20,label="",widget=TextInput(attrs={'placeholder':'Enter password','class':'form-control'}))


class Citizen(forms.Form):
    fname = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter First name "}),label="")
    lname= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Last name "}),label="")
    pob= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter place of birth "}),label="")
    fpob = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter  father's place of birth "}),label="")
    chief= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter chief's name "}),label="")
    postal= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter postal address "}),label="")
    dob= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter date of birth "}),label="")
    gender= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter gender "}),label="")
    village = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter village "}),label="")
    province = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter province "}),label="")
    nrc = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Nrc "}),label="")
    cob = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter country of birth "}),label="")
    fdob= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter father's date of birth "}),label="")
    district = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter District "}),label="")


# Citizen = formset_factory(Citz,extra=1)
