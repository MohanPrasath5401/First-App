from django import forms  
from .models import Student,MasterData,Mark_attendance
  
class Studentform(forms.Form):
 ID = forms.CharField(max_length=100)
 name = forms.CharField(max_length=100,label="NAME")
 email = forms.CharField(max_length=100)
 Class = forms.CharField(max_length=100)


 def clean_name(self):
    valname = self.cleaned_data['name']
    if len(valname)<4:
        raise forms.ValidationError("Enter more than or equal to 4")
    return valname

class Studentform1(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['stuid','stuname','stumail','stuclass']


class Masterform(forms.ModelForm):
    class Meta:
        model = MasterData
        fields = ['stuid','stuname','stumail','subject']

class MarkAttendance(forms.ModelForm):
    class Meta:
        model = Mark_attendance
        fields =['uid','subject_name']


class OneStudentform(forms.Form):
  ID = forms.IntegerField()



























