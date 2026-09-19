from django import forms
from .models import Student, Course, Marks


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name', 'last_name', 'roll_number', 'email',
            'phone', 'date_of_birth', 'gender', 'course', 'is_active',
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_roll_number(self):
        """TOPIC: Custom Validation — ensure roll number has no spaces."""
        roll_number = self.cleaned_data['roll_number']
        if ' ' in roll_number:
            raise forms.ValidationError("Roll number cannot contain spaces.")
        return roll_number


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']


class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['subject', 'score']


class StudentSearchForm(forms.Form):
    """TOPIC: Search Form — used on the student list page to filter results."""
    query = forms.CharField(
        required=False,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Search by name, roll no, or email...'})
    )
