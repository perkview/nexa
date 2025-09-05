from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),       # ✅ no leading slash
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("privacy/", views.privacy, name="privacy"),
    path("terms/", views.terms, name="terms"),
    path("submit_problem/", views.submit_problem, name="submit_problem"),
]
