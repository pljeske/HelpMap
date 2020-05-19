# Generated by Django 3.0.6 on 2020-05-19 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnreadMessagesFrom',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='unread_user', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('unread_from', models.ManyToManyField(related_name='unread_from', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='unread_messages',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.UnreadMessagesFrom'),
        ),
    ]
