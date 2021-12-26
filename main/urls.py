from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('form/', views.formview, name="Create_main"),
    path('form/complete/', views.Complete_View.as_view(), name="Complete"),
]