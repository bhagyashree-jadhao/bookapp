# Generated by Django 3.2.2 on 2021-10-29 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('author_name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=80)),
                ('published_date', models.DateField()),
            ],
        ),
    ]
