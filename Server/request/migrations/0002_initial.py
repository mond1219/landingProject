# Generated by Django 4.0.3 on 2022-04-29 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cus_req',
            name='user_uid',
            field=models.ForeignKey(db_column='user_uid', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='req_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
