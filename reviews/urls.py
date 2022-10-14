from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("create/", views.create, name="create"),
    path("index/", views.index, name="index"),
    path("update/<int:_pk>", views.update, name="update"),
    path("detail/<int:_pk>", views.detail, name="detail"),
    path("delete/<int:pk>", views.delete, name="delete"),
]
