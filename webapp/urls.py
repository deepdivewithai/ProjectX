from django.urls import path
from . import views

app_name = "webapp"

urlpatterns = [
    path("", views.landing_page, name="home"),
    path("register", views.register, name="register"),
    path("login", views.my_login, name="login"),
    path("logout", views.user_logout, name="logout"),
    # CRUD
    path("dashboard", views.dashboard, name="dashboard"),
    path("view-record/<int:pk>", views.view_record, name="record"),
    path("create-record", views.create_record, name="create"),
    path("update-record/<int:pk>", views.update_record, name="update"),
    path("delete-record/<int:pk>", views.delete_record, name="delete"),
]
