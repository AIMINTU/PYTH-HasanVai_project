
from django.contrib import admin
from django.urls import path
from bookms import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("get-all-books/",views.getAllBooks),#List
    path("add/",views.addBooksms),#new data add korar janno
    path("delete/<int:id>",views.delete),
    path("edit/<int:id>",views.edit),
    path("update/<int:id>",views.update)
]
