from django.urls import path
from . import views
urlpatterns = [
    path("", views.frontpage.as_view(), name = "frontpage"),
    path("privacy/", views.privacy.as_view(), name = "privacy"),
    path("terms/", views.terms.as_view(), name = "terms"),
    path("plans/", views.plans.as_view(), name = "plans"),
]
