from email import message
from re import template
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.template import context
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import CustomUser, ExchangeInfoModel, Thread, article_form, reportModel
from .forms import ExchangeInfoForm, PostUpdateForm, ReportForm, ThreadForm, UserCreationForm, categorie_form, LoginForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

#HOME

class IndexView(TemplateView):
    template_name = 'index.html'

#投稿完了

class Complete_View(TemplateView):
    template_name = 'complete.html'

#投稿作成

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
       return redirect('main:Create_Main')

#投稿編集

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = article_form
    form_class = PostUpdateForm
    template_name = 'update.html'
    def form_valid(self, form):
        messages.success(self.request, '更新が完了しました')
        return super(PostUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('main:List', kwargs={'pk': self.object.id})

    def form_invalid(self, form):
        messages.warning(self.request, '更新が失敗しました')
        return reverse_lazy('main:Update', kwargs={'pk':self.object.id})

#投稿削除

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = article_form
    template_name = 'delete.html'
    success_url = reverse_lazy('main:Article_List')
    success_message = "投稿を削除しました"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PostDeleteView, self).delete(request, *args, **kwargs)

#投稿一覧

class Article_list(ListView):
    template_name = 'article_list.html'
    model = article_form
    ordering = ['-date']

class Article_detail(DetailView):
    template_name = 'detail.html'
    model = article_form
    context_object_name = 'object'
    queryset = article_form.objects.all()
    
#サインアップ

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

#ログイン画面

class MyLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

#ログアウト画面

class MyLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'logout.html'

#サインアップ完了

class signupcomplete(TemplateView):
    template_name = 'signup_complete.html'

#違反報告

class ReportView(LoginRequiredMixin, CreateView):
    form_class = ReportForm
    template_name = 'report.html'
    success_url = reverse_lazy('main:Report_Comp')
    login_url = 'login/'
   
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, '投稿が完了しました')
        return super(ReportView, self).form_valid(form)
   
    def form_invalid(self, form):
        messages.warning(self.request, '投稿が失敗しました')
        return redirect('main:Report')

#報告完了

class ReportCompView(TemplateView):
    template_name = 'report_comp.html'

#情報交換掲示板

#スレッド一覧

def threads_list(request):
    threads = Thread.objects.all().values()
    count = len(threads)
    for count in range(count):
        username_dicts = CustomUser.objects.filter(pk=threads[count]['user_id']).values('username')
        threads[count].update(username_dicts[0])
    
    form = ThreadForm

    paginator = Paginator(threads, 9)
    current_page = request.GET.get('current_page')
    threads = paginator.get_page(current_page)
    context = {
        'threads': threads,
        'form': form,
    }
    return render(request, 'threads_list.html', context)

#スレッド作成

def create_thread(request):
    form = ThreadForm(request.POST)

    if form.is_valid():
        thread = form.save(commit=False)
        thread.user = request.user

        thread.save()
        messages.success(request, "スレッドを作成しました")
    else:
        print("バリデーションエラー")
    return redirect('main:Threads_List')

#レス一覧

def comments_list(request, thread_id):
    threads = Thread.objects.filter(pk=thread_id).values()
    thread = threads[0]
    username_dicts = CustomUser.objects.filter(pk=threads[0]['user_id']).values('username')
    thread.update(username_dicts[0])

    comments = ExchangeInfoModel.objects.filter(thread_id=thread_id).values()
    count = len(comments)

    for count in range(count):
        username_dicts = CustomUser.objects.filter(pk=comments[count]['user_id']).values('username')
        comments[count].update(username_dicts[0])
    
    form = ExchangeInfoForm
    context = {
        'thread': thread,
        'comments': comments,
        'form': form,
    }
    return render(request, 'comments_list.html', context)
    
#レス作成

def create_comment(request):
    thread_id = request.POST['thread_id']
    form = ExchangeInfoForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)

        comment.user = request.user
        comment.thread_id = thread_id
        comment.save()
        messages.success(request, "送信が完了しました")

    return redirect('main:Comments_List', thread_id=thread_id)