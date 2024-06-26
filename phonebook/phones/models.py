from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator
from django.conf import settings


class MyBaseModel(models.Model):
    is_active = models.BooleanField(
        default=False,
        verbose_name="Is Active",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At",
    )

    class Meta:
        abstract = True
        ordering = ("pk",)

    def __str__(self):
        raise NotImplementedError("Implement __str__ method")


class City(MyBaseModel):
    title = models.CharField(max_length=250, null=False,
                             blank=False, verbose_name="Title")

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"
        ordering = ("id",)

    def __str__(self) -> str:
        return self.title


class Phone(MyBaseModel):
    first_name = models.CharField(max_length=250, null=False,
                                  blank=False, verbose_name="FirstName")
    last_name = models.CharField(max_length=250, null=False,
                                 blank=False, verbose_name="LastName")
    mobile = models.CharField(max_length=11, null=False,
                              blank=False, verbose_name="Mobile", validators=[MinLengthValidator(11)])
    city = models.ForeignKey(City, null=False, blank=False,
                             on_delete=models.CASCADE, related_name="phones", verbose_name="City")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, default=1,
                               on_delete=models.CASCADE, related_name="phones", verbose_name="Author")

    class Meta:
        verbose_name = "Phone"
        verbose_name_plural = "Phones"
        ordering = ("id",)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        # return reverse("phone_detail", kwargs={"pk": self.pk})
        return reverse("phone_list")
