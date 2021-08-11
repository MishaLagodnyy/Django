from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *

class AddOrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['clientId'].empty_label ="Выберите клиента"
        self.fields['courierId'].empty_label = "Выберите Вашу фамилию"
        self.fields['priceId'].empty_label = "Выберите услугу"
    class Meta:
        model = Order
        fields = ['clientId','courierId', 'priceId', 'order_status']
        widgets = {
            # 'clientId' = forms.ModelChoiceField(label="Клиент",empty_label="Выберите клиента"),
            # 'courierId' = forms.ModelChoiceField(label="Курьер", empty_label="Выберите Вашу фамилию"),
            # 'priceId' = forms.ModelChoiceField(label="Услуга", empty_label="Выберите услугу"),
            # 'order_status' = forms.BooleanField(label="Завершить заказ", required=False, initial=True),
        }
    def clean_order_status(self):
        order_status = self.cleaned_data['order_status']
        if order_status == 'False':
            raise ValidationError('Заказ уже выполнен')

class GreatOrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['thing'].empty_label = "Выберите вещь"
        self.fields['service'].empty_label = "Выберите услугу"

    class Meta:
        model = Prices
        fields = ['thing','service']
    # def clean_order_status(self):
    #     order_status = self.cleaned_data['order_status']
    #     if order_status == 'False':
    #         raise ValidationError('Заказ уже выполнен')

class AddClientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].empty_label = "Имя"
        self.fields['patronymic'].empty_label = "Отчество"
        self.fields['lastname'].empty_label = "Фамилия"
        self.fields['tel'].empty_label = "телефон"
        self.fields['street'].empty_label = "улица"
        self.fields['house'].empty_label = "дом"
        self.fields['building'].empty_label = "строение"
        self.fields['entrance'].empty_label = "подъезд"
        self.fields['flat'].empty_label = "квартира"



        # name = models.CharField(max_length=255, verbose_name='Имя')
        # patronymic = models.CharField(max_length=255, verbose_name='Отчество')
        # lastname = models.CharField(max_length=255, verbose_name='Фамилия')
        # tel = models.IntegerField(verbose_name="телефон")
        # street = models.CharField(max_length=255, verbose_name="улица")
        # house = models.PositiveIntegerField(verbose_name="дом")
        # building = models.CharField(max_length=5, verbose_name="строение")
        # entrance = models.PositiveIntegerField(verbose_name="подъезд")
        # flat = models.PositiveIntegerField(verbose_name="квартира")
        # email = models.EmailField(max_length=254)

    class Meta:
        model = Client
        fields = ['name','patronymic', 'lastname', 'tel', 'street', 'house', 'building', 'entrance', 'flat']

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


