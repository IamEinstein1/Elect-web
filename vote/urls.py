from django.urls import path
from . import views
app_name = "voting"
urlpatterns = [
    # path('', views.templater, name="template"),
    path('', views.ip, name="ip"),
    # path('email/', views.email, name="mail"),
    path('logic/', views.logic, name="logic"),
    path('index/', views.index, name="index"),
    path('voted/', views.voted, name="voted"),
    path('thanks/', views.thanks, name="thanks"),
    path('aspl/', views.aspl, name="aspl"),
    path('spl/', views.spl, name="spl"),
    path('result/', views.result, name="result"),
    path('login/', views.login, name="login"),

]
