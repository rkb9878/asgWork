# Generated by Django 3.2 on 2021-04-20 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('manageAPI', '0002_business_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='business',
            field=models.ForeignKey(null=True, on_delete=django.db.models.fields.CharField, to='manageAPI.business'),
        ),
        migrations.AddField(
            model_name='products',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
