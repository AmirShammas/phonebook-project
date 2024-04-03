from django.urls import path
from .views import PhoneCreateView, PhoneDeleteView, PhoneDetailView, PhoneListView, HomePageView, PhoneUpdateView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("phone/", PhoneListView.as_view(), name="phone_list"),
    path("phone/<int:pk>/", PhoneDetailView.as_view(), name="phone_detail"),
    path("phone/new/", PhoneCreateView.as_view(), name="phone_new"),
    path("phone/<int:pk>/edit/", PhoneUpdateView.as_view(), name="phone_edit"),
    path("phone/<int:pk>/delete/", PhoneDeleteView.as_view(), name="phone_delete"),
]
