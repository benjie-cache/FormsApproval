# Generated by Django 4.0.3 on 2022-07-24 08:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('access', '0004_alter_rmsgeneralinformationprocess_date_approved_by_department_head_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rmsgeneralinformationprocess',
            name='applicant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
