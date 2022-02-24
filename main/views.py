from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from .models import CustomUser, NewsComments, NewsModel, article_form, reportModel
from .forms import NewsCommentForm, NewsForm, ReportForm, UserCreationForm, categorie_form, LoginForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

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

    def get_queryset(self):
        keyword = self.request.GET.get('keyword')
        queryset = article_form.objects.order_by('-date')
        category = self.request.GET.get('category')
        num = self.request.GET.get('num')
        vc = self.request.GET.get('vc')
        hard = self.request.GET.get('hard')

        if keyword:
            if category:
                if num:
                    if vc:
                        if hard:
                            queryset = queryset.filter(
                                title__icontains=keyword, per=category, num=num, vc=vc, hard=hard
                            )
                            messages.success(self.request, 'モード :「{}」 '.format(category) + '人数 :「{}」 '.format(num) + 'VC :「{}」 '.format(vc) + 'プレイ環境 :「{}」 '.format(hard) + '「{}」の検索結果'.format(keyword))
                        else:
                            queryset = queryset.filter(
                                title__icontains=keyword, per=category, num=num, vc=vc
                            )
                            messages.success(self.request, 'モード :「{}」 '.format(category) + '人数 :「{}」 '.format(num) + 'VC : 「{}」 '.format(vc) + '「{}」の検索結果'.format(keyword))
                    elif hard:
                        queryset = queryset.filter(
                            title__icontains=keyword, per=category, num=num, hard=hard
                        )
                        messages.success(self.request, 'モード :「{}」 '.format(category) + '人数 :「{}」 '.format(num) + 'プレイ環境 :「{}」 '.format(hard) + '「{}」の検索結果'.format(keyword))                       
                    else:
                        queryset = queryset.filter(
                            title__icontains=keyword, per=category, num=num
                        )
                        messages.success(self.request, 'モード :「{}」 '.format(category) + '人数 :「{}」 '.format(num) + '「{}」の検索結果'.format(keyword))
                elif vc:
                    if hard:
                        queryset = queryset.filter(
                            title__icontains=keyword, per=category, vc=vc, hard=hard
                        )
                        messages.success(self.request, 'モード :「{}」 '.format(category) + 'プレイ環境 :「{}」 '.format(hard) + '「{}」の検索結果'.format(keyword))
                    else:
                        queryset = queryset.filter(
                            title__icontains=keyword, per=category, vc=vc
                            )
                        messages.success(self.request, 'モード :「{}」 '.format(category) + 'VC :「{}」 '.format(vc) + '「{}」の検索結果'.format(keyword))
                elif hard:
                        queryset = queryset.filter(
                            title__icontains=keyword, per=category, hard=hard
                        )
                        messages.success(self.request, 'モード :「{}」 '.format(category) + 'プレイ環境 :「{}」 '.format(hard) + '「{}」の検索結果'.format(keyword))
                else:
                    queryset = queryset.filter(
                        per=category, title__icontains=keyword
                    )
                    messages.success(self.request, 'モード :「{}」 '.format(category) + '「{}」の検索結果'.format(keyword))

            elif num:
                if vc:
                    if hard:
                        queryset = queryset.filter(
                            title__icontains=keyword, num=num, vc=vc, hard=hard
                        )
                        messages.success(self.request, '人数 :「{}」 '.format(num) + 'VC :「{}」 '.format(vc) + 'プレイ環境 :「{}」'.format(hard) + '「{}」の検索結果'.format(keyword))
                    else:
                        queryset = queryset.filter(
                            title__icontains=keyword, num=num, vc=vc
                        )
                        messages.success(self.request, '人数 :「{}」 '.format(num) + 'VC : 「{}」 '.format(vc) + '「{}」の検索結果'.format(keyword))
                elif hard:
                        queryset = queryset.filter(
                            title__icontains=keyword, num=num, hard=hard
                        )
                        messages.success(self.request, '人数 :「{}」 '.format(num) + 'プレイ環境 :「{}」 '.format(hard) + '「{}」の検索結果'.format(keyword))
                else:
                    queryset = queryset.filter(
                        num=num, title__icontains=keyword
                    )
                    messages.success(self.request, '人数 :「{}」 '.format(num) + '「{}」の検索結果'.format(keyword))

            elif vc:
                if hard:
                        queryset = queryset.filter(
                            title__icontains=keyword, vc=vc, hard=hard
                        )
                        messages.success(self.request, 'VC :「{}」 '.format(vc) + 'プレイ環境 :「{}」 '.format(hard) + '「{}」の検索結果'.format(keyword))
                else:
                    queryset = queryset.filter(
                        vc=vc, title__icontains=keyword
                    )
                    messages.success(self.request, 'VC :「{}」 '.format(vc) + '「{}」の検索結果'.format(keyword))
    
            elif hard:
                queryset = queryset.filter(
                    hard=hard, title__icontains=keyword
                )
                messages.success(self.request, 'プレイ環境 :「{}」 '.format(hard) + '「{}」の検索結果'.format(keyword))
            else:
                queryset = queryset.filter(
                    title__icontains=keyword
                )
                messages.success(self.request, '「{}」の検索結果'.format(keyword))

        if category:
            if num:
                if vc:
                    if hard:
                        queryset = queryset.filter(
                            per=category, num=num, vc=vc, hard=hard
                        )
                        messages.success(self.request,'モード :「{}」 '.format(category) + '人数 :「{}」 '.format(num) + 'VC :「{}」 '.format(vc) + 'プレイ環境 :「{}」の検索結果'.format(hard))
                    else:
                        queryset = queryset.filter(
                            per=category, num=num, vc=vc
                        )
                        messages.success(self.request,'モード :「{}」 '.format(category) + '人数 :「{}」 '.format(num) + 'VC : 「{}」の検索結果'.format(vc))
                elif hard:
                        queryset = queryset.filter(
                            per=category, num=num, hard=hard
                        )
                        messages.success(self.request,'モード :「{}」 '.format(category) + '人数 :「{}」 '.format(num) + 'プレイ環境 :「{}」の検索結果'.format(hard))
                else:
                    queryset = queryset.filter(
                        per=category, num=num
                    )
                    messages.success(self.request, 'モード :「{}」 '.format(category) + '人数 :「{}」の検索結果'.format(num))
            elif vc:
                if hard:
                    queryset = queryset.filter(
                        per=category, vc=vc, hard=hard
                    )
                    messages.success(self.request, 'モード :「{}」 '.format(category) + 'VC :「{}」 '.format(vc) + 'プレイ環境 :「{}」の検索結果'.format(hard))
                else:
                    queryset = queryset.filter(
                        per=category, vc=vc
                    )
                    messages.success(self.request, 'モード :「{}」 '.format(category) + 'VC :「{}」の検索結果'.format(vc))
            elif hard:
                queryset = queryset.filter(
                    per=category, hard=hard
                )
                messages.success(self.request, 'モード :「{}」 '.format(category) + 'プレイ環境 :「{}」の検索結果'.format(hard))
            else:
                queryset = queryset.filter(
                    per=category
                )
                messages.success(self.request, 'モード :「{}」の検索結果'.format(category))

        if num:
            if vc:
                if hard:
                    queryset = queryset.filter(
                        num=num, vc=vc, hard=hard
                    )
                    messages.success(self.request, '人数 :「{}」'.format(num) + 'VC :「{}」'.format(vc) + 'プレイ環境 :「{}」の検索結果'.format(hard))
                else:
                    queryset = queryset.filter(
                        num=num, vc=vc
                    )
                    messages.success(self.request, '人数 :「{}」'.format(vc) + 'VC : 「{}」の検索結果'.format(vc))
            elif hard:
                queryset = queryset.filter(
                    num=num, hard=hard
                )
                messages.success(self.request, '人数 :「{}」'.format(num) + 'プレイ環境 :「{}」の検索結果'.format(hard))
            else:
                queryset = queryset.filter(
                    num=num
                )
                messages.success(self.request, '人数 :「{}」の検索結果'.format(num))

        if vc:
            if hard:
                queryset = queryset.filter(
                    vc=vc, hard=hard
                )
                messages.success(self.request, 'VC :「{}」'.format(vc) + 'プレイ環境 :「{}」の検索結果'.format(hard))
            else:
                queryset = queryset.filter(
                    vc=vc
                )
                messages.success(self.request, 'VC :「{}」の検索結果'.format(vc))
            
        if hard:
            queryset = queryset.filter(
                hard=hard
            )
            messages.success(self.request, 'プレイ環境 :「{}」の検索結果'.format(hard))

        return queryset


class Article_detail(DetailView):
    template_name = 'detail.html'
    model = article_form
    context_object_name = 'object'
    queryset = article_form.objects.all()
    
#サインアップ

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            password = form.cleaned_data.get('password1')
            user = form.save(commit=False)
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

class ReportView(CreateView):
    model = reportModel
    form_class = ReportForm
    template_name = 'report.html'
    success_url = reverse_lazy('main:Article_List')
   
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, '報告が完了しました')
        return super(ReportView, self).form_valid(form)
   
    def form_invalid(self, form):
        messages.warning(self.request, '報告に失敗しました')
        return redirect('main:Report')

#報告完了

class ReportCompView(TemplateView):
    template_name = 'report_comp.html'

#News作成

class NewsCreateView(CreateView):
    template_name = 'news_list.html'
    form_class = NewsForm
    success_url = reverse_lazy('main:News_List')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect('main:News_List')

#News一覧

class NewsListView(ListView):
    model = NewsModel
    template_name = 'news_list.html'
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['news_form'] = NewsCreateView

        return context
        

    def get_queryset(self):
        queryset = NewsModel.objects.order_by('-date')
        keyword = self.request.GET.get('keyword')

        if keyword:
            queryset = queryset.filter(
                            title__icontains=keyword
                       )
            messages.success(self.request, '「{}」の検索結果'.format(keyword))

        return queryset
    
class NewsDetailView(LoginRequiredMixin, DetailView):
    model = NewsModel
    template_name = 'news_detail.html'
    queryset = NewsModel.objects.all()
    login_url = 'login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['comment_form'] = NewsCommentForm

        return context

#コメント作成view

class NewsCommentView(CreateView):
    model = NewsComments
    form_class = NewsCommentForm

    def form_valid(self, form):
        post_pk = self.kwargs.get('pk')
        post = get_object_or_404(NewsModel, pk=post_pk)
        form.instance.user = self.request.user
        comment = form.save(commit=False)
        comment.news = post
        comment.save()
        messages.success(self.request, '投稿が完了しました')
        return redirect('main:News_Detail', pk=post_pk)

#Search.htmlリスト

class SearchListView(ListView):
    model = article_form
    template_name = "Search.html"
    
    def get_context_data(self, **kwargs):
        context = super(SearchListView, self).get_context_data(**kwargs)
        context.update({
            'user':CustomUser.objects.all(),
            'news': NewsModel.objects.all()
        })
        return context



class UserListView(ListView):
    model = CustomUser
    template_name = "user_list.html"

    def get_queryset(self):
        queryset = CustomUser.objects.all()
        keyword = self.request.GET.get('keyword')
        rank = self.request.GET.get('rank')
        hard = self.request.GET.get('hard')
        character = self.request.GET.get('character')
        
        if keyword:
            if rank:
                if hard:
                    if character:
                        queryset = queryset.filter(
                            (Q(player_name__icontains=keyword) | Q(username__icontains=keyword)),
                            rank=rank, playfield__icontains=hard, character__icontains=character 
                        )
                    else:
                        queryset = queryset.filter(
                            (Q(player_name__icontains=keyword) | Q(username__icontains=keyword)),
                            rank=rank, playfield__icontains=hard
                        )
                elif character:
                    queryset = queryset.filter(
                        (Q(player_name__icontains=keyword) | Q(username__icontains=keyword)),
                        rank=rank, character__icontains=character
                    )
                else:
                    queryset = queryset.filter(
                        (Q(player_name__icontains=keyword) | Q(username__icontains=keyword)),
                        rank=rank
                    )
            elif hard:
                if character:
                    queryset = queryset.filter(
                        (Q(player_name__icontains=keyword) | Q(username__icontains=keyword)),
                        playfield__icontains=hard, character__icontains=character
                    )
                else:
                    queryset = queryset.filter(
                        (Q(player_name__icontains=keyword) | Q(username__icontains=keyword)),
                        playfield__icontains=hard
                    )
            elif character:
                queryset = queryset.filter(
                    (Q(player_name__icontains=keyword) | Q(username__icontains=keyword)),
                    character__icontains=character
                )
            else:
                queryset = queryset.filter(
                    Q(player_name__icontains=keyword) | Q(username__icontains=keyword)
                )
        elif rank:
            if hard:
                if character:
                    queryset = queryset.filter(
                        rank=rank, playfield__icontains=hard, characte__icontainsr=character
                    )
                else:
                    queryset = queryset.filter(
                        rank=rank, playfield__icontains=hard
                    )
            elif character:
                queryset = queryset.filter(
                    rank=rank, character__icontains=character
                )
            else:
                queryset = queryset.filter(
                    rank=rank
                )
        elif hard:
            if character:
                queryset = queryset.filter(
                    playfield__icontains=hard, character__icontains=character
                )
            else:
                queryset = queryset.filter(
                    playfield__icontains=hard
                )
        elif character:
            queryset = queryset.filter(
                character__icontains=character
            )
        return queryset

class UserDetailView(DetailView):
    model = CustomUser
    template_name = 'user_detail.html'
    queryset = CustomUser.objects.all()