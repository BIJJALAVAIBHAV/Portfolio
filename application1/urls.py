from django.contrib import admin
from django.urls import path,include
from application1 import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('projects/',views.project, name='project'),
    path('contact/',views.contact, name='contact'),
    path('login/',views.login,name='login'),
    path('feedbacks/', views.queries, name='queries'),
    path('feedback/<int:id>/', views.viewdata, name='feedback-detail'),

]