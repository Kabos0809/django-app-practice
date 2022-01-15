from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import article_form
from .forms import PostUpdateForm, UserCreationForm, categorie_form, LoginForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(TemplateView):
    template_name = 'index.html'

class Complete_View(TemplateView):
    template_name = 'complete.html'

class PostCreateView(LoginRequiredMixin, CreateView):
   template_name = 'forms.html'
   form_class = categorie_form
   success_url = reverse_lazy('main:Complete')
   login_url = 'login/'
   
   def form_valid(self, form):
       form.instance.user = self.request.user
       messages.success(self.request, '投稿が完了しました')
       return super(PostCreateView, self).form_valid(form)
   
   def form_invalid(self, form):
       messages.warning(self.request, '投稿が失敗しました')
       return redirect('main:Create_main')

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = article_form
    form_class = PostUpdateForm
    template_name = 'update.html'
    def form_valid(self, form):
        messages.success(self.request, '更新が完了しました')
        return super(PostUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('main:list', kwargs={'pk': self.object.id})

    def form_invalid(self, form):
        messages.warning(self.request, '更新が失敗しました')
        return reverse_lazy('main:update', kwargs={'pk':self.object.id})

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