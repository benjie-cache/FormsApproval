# Generated by Django 4.0.5 on 2022-10-13 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0028_alter_rmsgeneralinformationprocess_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rmsgeneralinformationprocess',
            name='Date',
            field=models.DateField(null=True),
        ),
    ]
