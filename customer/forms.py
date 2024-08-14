from django import forms
from django.contrib.auth.models import User
from customer.models import Customer


class CustomerUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone']


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=200)

    def clean_email(self):
        email = self.data.get['email']
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError(f'That {email} does not exist')
        return email

    def clean_password(self):
        email = self.data.get('email')
        password = self.data.get('password')
        try:
            user = User.objects.get(email=email)
            print(user)
            if not user.check_password(password):
                raise forms.ValidationError(f'that {email} does not exist')
        except User.DoesNotExist:
            raise forms.ValidationError(f'That email {email} does not exist')
        return password


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=200)

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone', 'address']

    def clean_email(self):
        email = self.data.get['email']
        if Customer.objects.filter(email=email).exists():
            raise forms.ValidationError(f'That email {email} already exists')
        return email

    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError(f'Passwords do not match')
        return password
