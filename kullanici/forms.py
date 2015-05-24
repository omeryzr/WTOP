__author__ = 'omr24'

from django import forms
from models import *

class new_member_form(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'