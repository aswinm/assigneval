from django import forms
from assignment.models import Assignment,Submission

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('name','sample_copy','deadline')
        widgets = {
                'deadline': forms.DateTimeInput(attrs={'placeholder':"Y-m-d H:M:S"})
                }

class SubForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ('assignment','answer')
