from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView
from .models import Phone


class HomePageView(TemplateView):
    template_name = "home.html"


class PhoneListView(LoginRequiredMixin, ListView):
    model = Phone
    context_object_name = "phone_list"
    template_name = "phones/phone_list.html"
    login_url = "login"


class PhoneDetailView(LoginRequiredMixin, DetailView):
    model = Phone
    context_object_name = "phone"
    template_name = "phones/phone_detail.html"
    login_url = "login"


# class PhoneUpdateView(UpdateView): 
#     model = Phone
#     fields = (
#         "first_name",
#         "body",
#     )
#     template_name = "phones/phone_edit.html"
