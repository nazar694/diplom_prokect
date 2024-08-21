# Generated by Django 3.2.7 on 2021-12-05 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='small_desk',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='title',
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(default='NONE', max_length=35, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(default='NONE', max_length=45, verbose_name='Категорія'),
        ),
        migrations.AddField(
            model_name='blog',
            name='full_desk',
            field=models.TextField(default='NONE', max_length=500, verbose_name='Повний опис'),
        ),
        migrations.AddField(
            model_name='blog',
            name='name',
            field=models.CharField(default='NONE', max_length=35, verbose_name='Назва'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]