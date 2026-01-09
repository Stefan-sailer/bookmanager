from django.urls import path
from book.views import index, set_cookie
from django.urls.converters import register_converter
from . import views
from book.views import shop, register, json

class mobileConverter:
    regex = '1[3-9]\d{9}'

    def to_python(self, value):
        return int(value)

    # def to_url(self, value):
    #     return str(value)

register_converter(mobileConverter, "phone")


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:local_id>/<phone:shop_id>', shop),
    path('register/', register),
    path('json/', json),
    path('set_cookie/', set_cookie)
]