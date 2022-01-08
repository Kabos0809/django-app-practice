from datetime import date
from re import template
from django.contrib.auth import authenticate, login as auth_login, get_user_model
from django.db.models import query
from django.contrib import messages
from django.http import request
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render, redirect
from .models import CustomUser, article_form
from .forms import UserCreationForm, categorie_form, LoginForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

User = get_user_model()

class IndexView(TemplateView):
    template_name = 'index.html'

class Complete_View(TemplateView):
    template_name = 'complete.html'

def formview(request):
    form = categorie_form()
    context = {'form' : form}

    #copied = request.POST.copy()
    #copied['author'] = request.author.username

    if request.method == 'POST':
        data = request.POST
        title = data['title']
        rnk_min = data['rnk_min']
        rnk_max = data['rnk_max']
        num = data['num']
        per = data['per']
        comments = data['comments']
        hard = data['hard']

        article_form.objects.create(
            title = title,
            rnk_min = rnk_min,
            rnk_max = rnk_max,
            num = num,
            per = per,
            comments = comments,
            hard = hard,
        )
        return redirect('complete/')
    return render(request, 'form.html', context)

class Article_list(ListView):
    template_name = 'article_list.html'
    model = article_form
    ordering = ['-date']

class Article_detail(DetailView):
    template_name = 'detail.html'
    model = article_form
    context_object_name = 'object'
    queryset = article_form.objects.all()

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password1')
            user = form.save()

            user.set_password(password)
            user.save()

            auth_login(request, user)
            return redirect('signup_complete/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})

class MyLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

class MyLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'logout.html'

class signupcomplete(TemplateView):
    template_name = 'signup_complete.html'