from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('podcast/', views.podcasts, name='podcasts'),
    # path('podcast/<slug:slug>/', views.podcast, name='podcast'),
    path('blog/', views.blogs, name='blogs'),
    path('blog/<slug:slug>/', views.blog, name='blog'),
    path('blog/category/<slug:slug>/', views.category, name='category'),

]