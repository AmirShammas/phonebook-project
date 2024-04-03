# Generated by Django 4.2 on 2024-04-03 10:10

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("phones", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="phone",
            name="author",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="phones",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Author",
            ),
        ),
        migrations.AlterField(
            model_name="phone",
            name="mobile",
            field=models.CharField(
                max_length=11,
                validators=[django.core.validators.MinLengthValidator(11)],
                verbose_name="Mobile",
            ),
        ),
    ]