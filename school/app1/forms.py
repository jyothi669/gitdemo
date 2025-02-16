from django import forms
from app1.models import School

class SchoolForm(forms.ModelForm):
    location_choices=[('ernamkulam','EKM'),('Kollam','KOLLAM'),('trivandrum','TVM')]

    class Meta:
        model=School
        fields=['name','location','principal']