# Generated by Django 3.2 on 2021-04-21 01:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('manageAPI', '0007_auto_20210421_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='business',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.fields.CharField, to='manageAPI.business'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image1',
            field=models.ImageField(upload_to='product/'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image2',
            field=models.ImageField(upload_to='product/'),
        ),
        migrations.AlterField(
            model_name='products',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
