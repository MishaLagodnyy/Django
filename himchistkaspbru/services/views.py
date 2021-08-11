import logging

from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView

from services.forms import *
from services.models import *

log = logging.getLogger(__name__)

menu = [{'title': "О компании", 'url_name': 'about'},
        {'title': "Вопросы и ответы", 'url_name': 'questions_and_answers'},
        {'title': "Отзывы", 'url_name': 'review'},
        {'title': "Наши адреса", 'url_name': 'contact'},
        ]


class Service_Home(ListView):
    model = Post
    template_name = 'services/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        log.info("Успешно")
        return context
# def index(request):
#     posts = Post.objects.all()
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Главная страница'
#     }
#     return render(request, 'services/index.html', context=context)

def about(request):
    return render(request, 'services/about.html', {'menu': menu, 'title': 'О нас'})

class Service_Questions_And_Answers(ListView):
    model = Questions_And_Answers
    template_name = 'services/questions_and_answers.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Вопросы и ответы'
        return context

# def questions_and_answers(request):
#     posts = Questions_And_Answers.objects.all()
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Вопросы и ответы'
#     }
#     return render(request, 'services/questions_and_answers.html', context=context)

def contact(request):
    return render(request, 'services/contact.html', {'menu': menu, 'title': 'Наши адреса'})

class Service_Review(ListView):
    model = Reviews
    template_name = 'services/review.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Отзывы'
        return context
# def review(request):
#     posts = Reviews.objects.all()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Отзывы'
#     }
#     return render(request, 'services/review.html', context=context)
# def login(request):
#     return render(request, 'services/login.html', {'menu': menu, 'title': 'Войти'})



def pageNotFound(request, exception):
    return HttpResponseNotFound ("<h1>Страница не найдена!!!</h1>")

def addorder(request):
    if request.method == 'POST':
        form = AddOrderForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = AddOrderForm()
    return render(request, 'services/addorder.html', {'form': form, 'menu': menu, 'title': 'Завершить заказ'})

def greatorder(request):
    if request.method == 'POST':
        form = GreatOrderForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = GreatOrderForm()
    return render(request, 'services/greatorder.html', {'form': form, 'menu': menu, 'title': 'Сделать заказ'})

def addclient(request):
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = AddClientForm()
    return render(request, 'services/addclient.html', {'form': form, 'menu': menu, 'title': 'Внести свои данные'})

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'services/register.html'
    success_url = reverse_lazy('login')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Регистация'
        return context
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'services/login.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Войти'
        return context

    # def get_success_url(self):
    #     return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')