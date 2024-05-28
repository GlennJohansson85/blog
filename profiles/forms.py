from django import forms
from .models import Profile

#___________________________________________________________  RegistrationForm
class RegistrationForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Choose a strong password',
        'class': 'form-control',
    }))
    
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': '<-- The one you created',
    }))

    profile_picture = forms.ImageField(required=False, error_messages={'Invalid':("Image files only.")}, widget=forms.FileInput)
    
    class Meta:
        model  = Profile
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password',  'profile_picture']
        
        
    def clean(self):

        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match.')
    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'HoffMeister'
        self.fields['first_name'].widget.attrs['placeholder'] = 'David'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Hasselhoff'
        self.fields['email'].widget.attrs['placeholder'] = 'David.Hasselhoff@hotmail.com'
        self.fields['phone_number'].widget.attrs['placeholder'] = '+1 555-123-4567'
        self.fields['profile_picture'].required = False
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


#___________________________________________________________  UserForm
class UserForm(forms.ModelForm):

    profile_picture = forms.ImageField(required=False, error_messages={'Invalid':("Image files only.")}, widget=forms.FileInput)

    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'phone_number', 'profile_picture']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'