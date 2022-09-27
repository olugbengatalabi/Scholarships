from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("category", views.category_options, name="category_picker"),
    path("developer_applications", views.developer_form, name="developer_form")
]
