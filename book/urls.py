from django.urls import path
from book.views import index
from . import views
urlpatterns = [
    path('', views.index, name='index'),
]