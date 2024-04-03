from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Phone
from django.utils.decorators import method_decorator


def superuser_required(view_func):
    def decorated_view_func(request, *args, **kwargs):
        if not request.user.is_superuser:
            message = "<h1>Access Denied !! Back to <a href='/'>home</a> page !!</h1>"
            return HttpResponseForbidden(message)
        return view_func(request, *args, **kwargs)
    return decorated_view_func


class SuperuserPhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ["first_name", "last_name", "mobile", "city", "is_active"]


class RegularUserPhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ["first_name", "last_name", "mobile", "city"]


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


class PhoneCreateView(LoginRequiredMixin, CreateView):
    model = Phone
    context_object_name = "phone"
    template_name = "phones/phone_new.html"
    fields = ["first_name", "last_name", "mobile", "city"]
    login_url = "login"


class PhoneUpdateView(LoginRequiredMixin, UpdateView):
    model = Phone
    context_object_name = "phone"
    template_name = "phones/phone_edit.html"
    fields = ["first_name", "last_name", "mobile", "city"]
    login_url = "login"

    def get_form_class(self):
        if self.request.user.is_superuser:
            return SuperuserPhoneForm
        return RegularUserPhoneForm


@method_decorator(superuser_required, name='dispatch')
class PhoneDeleteView(LoginRequiredMixin, DeleteView):
    model = Phone
    context_object_name = "phone"
    template_name = "phones/phone_delete.html"
    success_url = reverse_lazy("phone_list")
