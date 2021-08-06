# Generated by Django 3.2.4 on 2021-08-06 08:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('NewsPaper', '0012_postcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcategory',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(blank=True, null=True, related_name='subscriber', to=settings.AUTH_USER_MODEL),
        ),
    ]