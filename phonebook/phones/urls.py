from django.urls import path
from .views import PhoneDetailView, PhoneListView, HomePageView     #, PhoneUpdateView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("phones/", PhoneListView.as_view(), name="phone_list"),
    path("phones/<int:pk>/", PhoneDetailView.as_view(), name="phone_detail"),
    # path("phones/<int:pk>/edit/", PhoneUpdateView.as_view(), name="phone_edit"),
]
