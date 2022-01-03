from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('form/', views.formview, name="Create_main"),
    path('form/complete/', views.Complete_View.as_view(), name="Complete"),
    path('list/', views.Article_list.as_view(), name='article_list'),
    path('detail/<uuid:pk>', views.Article_detail.as_view(), name='article_detail'),
    path('signup/', views.signup, name="sign_up"),
    path('login/', views.MyLoginView.as_view(), name="login"),
    path('logout/', views.MyLogoutView.as_view(), name="logout"),
    path('signup/signup_complete/', views.signupcomplete.as_view(), name="signup_complete"),
]