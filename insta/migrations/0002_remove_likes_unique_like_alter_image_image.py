# Generated by Django 4.0.4 on 2022-06-05 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='likes',
            name='unique_like',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='DEFAULT VALUE', upload_to='', verbose_name='pictures'),
        ),
    ]