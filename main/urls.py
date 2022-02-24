from django.urls import path
from . import views

#頭文字、アンダーバー後は大文字とすること

app_name = 'main'

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='Index'),
    path('form/', views.PostCreateView.as_view(), name="Create_Main"),
    path('form/complete/', views.Complete_View.as_view(), name="Complete"),
    path('list/', views.Article_list.as_view(), name='Article_List'),
    path('detail/<uuid:pk>', views.Article_detail.as_view(), name='Article_Detail'),
    path('signup/', views.signup, name="Sign_Up"),
    path('form/login/', views.MyLoginView.as_view(), name="Login"),
    path('logout/', views.MyLogoutView.as_view(), name="Logout"),
    path('signup/signup_complete/', views.signupcomplete.as_view(), name="Signup_Complete"),
    path('report/', views.ReportView.as_view(), name="Report"),
    path('report/login/', views.MyLoginView.as_view(), name="Report_Login"),
    path('report/report_comp/', views.ReportCompView.as_view(), name="Report_Comp"),
    path('delete/<uuid:pk>/', views.PostDeleteView.as_view(), name="Post_Delete"),
    path('news_create/', views.NewsCreateView.as_view(), name="News_Create"),
    path('news_list/', views.NewsListView.as_view(), name="News_List"),
    path('news_detail/<uuid:pk>/', views.NewsDetailView.as_view(), name="News_Detail"),
    path('news_detail/<uuid:pk>/login/', views.MyLoginView.as_view(), name="News_Detail_Login"),
    path('news_comment/<uuid:pk>/', views.NewsCommentView.as_view(), name="News_Comment"),
    path('search/', views.SearchListView.as_view(), name="Search"),
    path('userlist/', views.UserListView.as_view(), name="User_List"),
    path('userdetail/<uuid:pk>/', views.UserDetailView.as_view(), name="User_Detail"),
]