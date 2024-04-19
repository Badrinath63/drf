from django.urls import path
from .views import ContactListCreateView, ContactDetailView

urlpatterns = [
    path('contacts/', ContactListCreateView.as_view()),
    path('contacts/', ContactDetailView.as_view()),
]
