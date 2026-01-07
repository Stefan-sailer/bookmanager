from django.contrib import admin
from book.models import BookInfo, PeopleInfo


admin.site.register(BookInfo)
admin.site.register(PeopleInfo)
# Register your models here.
