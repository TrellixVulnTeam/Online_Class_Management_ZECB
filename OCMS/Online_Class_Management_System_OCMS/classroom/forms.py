from django import forms
from classroom.models import User,Teacher,Student,StudentMarks,MessageToTeacher,ClassNotice,ClassAssignment,SubmitAssignment,LiveClass,ClassTest, ClassMaterial
from django.contrib.auth.forms import UserCreationForm



## User Login Form (Applied in both student and teacher login)
class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username','password1','password2']
        widgets = {
                'username': forms.TextInput(attrs={'class':'answer'}),
                'password1': forms.PasswordInput(attrs={'class':'answer'}),
                'password2': forms.PasswordInput(attrs={'class':'answer'}),
                }
        
## Teacher Registration Form 
class TeacherProfileForm(forms.ModelForm):
    class Meta():
        model =  Teacher
        fields = ['name','phone','email','subject_name']
        widgets = {
                'name': forms.TextInput(attrs={'class':'answer'}),
                'email': forms.EmailInput(attrs={'class':'answer'}),
                'phone': forms.NumberInput(attrs={'class':'answer'}),
                'subject_name': forms.TextInput(attrs={'class':'answer'}),
                }

## Teacher Profile Update Form
class TeacherProfileUpdateForm(forms.ModelForm):
    class Meta():
        model = Teacher
        fields = ['name','subject_name','email','phone','teacher_profile_pic']

## Student Registration Form
class StudentProfileForm(forms.ModelForm):
    class Meta():
        model =  Student
        fields = ['name','roll_no','phone','email']
        widgets = {
                'name': forms.TextInput(attrs={'class':'answer'}),
                'roll_no': forms.NumberInput(attrs={'class':'answer'}),
                'phone': forms.NumberInput(attrs={'class':'answer'}),
                'email': forms.EmailInput(attrs={'class':'answer'}),
                }

## Student profile update form
class StudentProfileUpdateForm(forms.ModelForm):
    class Meta():
        model = Student
        fields = ['name','roll_no','email','phone','student_profile_pic']
        

## Writing message to teacher        
class MessageForm(forms.ModelForm):
    class Meta():
        model = MessageToTeacher
        fields = ['message']

## Writing notice in the class        
class NoticeForm(forms.ModelForm):
    class Meta():
        model = ClassNotice
        fields = ['message']

class DateInput(forms.DateInput):
    input_type = 'datetime-local'

# class exampleForm(forms.Form):
#     Deadline = forms.DateTimeField(widget=DateInput)
#     PublishedAt = forms.DateTimeField(widget=DateInput)

## Form for uploading or updating assignment (teachers only)       
class AssignmentForm(forms.ModelForm):
    class Meta():
        model = ClassAssignment
        fields = ['assignment_name','assignment', 'PublishedAt','Deadline']
        widgets = {
                # 'Deadline' : DateInput(),
                # 'PublishedAt' : forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'class':'datetimefield'}),
                # 'Deadline' : forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'class':'datetimefield'}),
                # 'hiddenstatus' : forms.CheckboxInput(attrs={'class':'answer'})
                'PublishedAt' : DateInput(),
                'Deadline' : DateInput(),
                }


## Form for uploading marks and also for updating it.
class MarksForm(forms.ModelForm):
    class Meta():
        model = StudentMarks
        fields = ['subject_name','marks_obtained','maximum_marks']

## Form for uploading or updating assignment (teachers only)       
class MaterialForm(forms.ModelForm):
    class Meta():
        model = ClassMaterial
        fields = ['material_name','material']

class LiveClassForm(forms.ModelForm):
    class Meta():
        model = LiveClass
        fields = ['ClassName', 'StartTime','EndTime']
        widgets = {
                # 'Deadline' : DateInput(),
                # 'PublishedAt' : forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'class':'datetimefield'}),
                # 'Deadline' : forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'class':'datetimefield'}),
                # 'hiddenstatus' : forms.CheckboxInput(attrs={'class':'answer'})
                'StartTime' : DateInput(),
                'EndTime' : DateInput(),
                }


class ClassTestForm(forms.ModelForm):
    class Meta():
        model = ClassTest
        fields = ['TestName', 'StartTime','EndTime', 'Testlink']
        widgets = {
                # 'Deadline' : DateInput(),
                # 'PublishedAt' : forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'class':'datetimefield'}),
                # 'Deadline' : forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'class':'datetimefield'}),
                # 'hiddenstatus' : forms.CheckboxInput(attrs={'class':'answer'})
                'StartTime' : DateInput(),
                'EndTime' : DateInput(),
                }
        

## Form for submitting assignment (Students only)        
class SubmitForm(forms.ModelForm):
    class Meta():
        model = SubmitAssignment
        fields = ['submit']