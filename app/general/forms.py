from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset, Field, HTML, Div
from .models import *


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Имя Пользователя',
                               widget=forms.TextInput(attrs={'placeholder': 'ИМЯ ПОЛЬЗОВАТЕЛЯ'}))
    firstName = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'placeholder': 'ИМЯ'}))
    surname   = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    email     = forms.CharField(label='E-mail', widget=forms.TextInput(attrs={'placeholder': 'E-MAIL'}))
    phone     = forms.CharField(label='Номер Телефона', required=False, widget=forms.TextInput(attrs={'placeholder': 'Номер Телефона'}))
    img       = forms.ImageField(label='Фотография', required=False)
    password  = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Повторите Пароль',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Повторите Пароль'}))

    class Meta:
        model = User
        fields = [
            'username',
            'firstName',
            'surname',
            'email',
            'phone',
            'img',
            'password',
        ]

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-registration-form'
        self.helper.form_action = "."
        self.helper.form_method = 'POST'
        self.helper.form_class = 'row justify-content-center mb-2'
        self.helper.layout = Layout(
            Fieldset("Регистрация",
                     Field('username', css_class='form-control  m-0 mb-2 py-1'),
                     Field('firstName',css_class='form-control  m-0 mb-2 py-1'),
                     Field('surname',css_class='form-control  m-0 mb-2 py-1'),
                     Field('email',css_class='form-control  m-0 mb-2 py-1'),
                     Field('phone',css_class='form-control  m-0 mb-2 py-1'),
                     Field('password', css_class='form-control  m-0 mb-2 py-1'),
                     Field('password2', css_class='form-control  m-0 mb-2 py-1'),
                     Div('img'),
                     Submit('submit', 'Зарегистроваться', css_class='col btn btn-primary my-2  text-white'),
                     HTML(
                         '<p class="row my-2 ml-1">Уже зарегистрированы?<a href="/login" class="ml-2 ">Войдите</a></p>'),
                     css_class='col-4 border my-3 p-3 border-dark'
                     )
        )

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('Пароли должены быть одинаковые')
        return password