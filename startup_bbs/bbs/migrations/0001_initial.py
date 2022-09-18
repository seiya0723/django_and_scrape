# Generated by Django 3.2.10 on 2022-09-18 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='名前')),
                ('comment', models.CharField(max_length=2000, verbose_name='コメント')),
            ],
        ),
    ]
