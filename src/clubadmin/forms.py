from django import forms
from .models import Programme, Group

class ProgrammeForm(forms.ModelForm):
    class Meta:
        model = Programme
        fields = ['name', 'duration']

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'programme', 'description']


from django import forms
from .models import Child

class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['first_name', 'last_name', 'group', 'birth_date', 'school_level']

