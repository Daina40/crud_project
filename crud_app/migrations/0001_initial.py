# Generated by Django 4.2.2 on 2023-06-20 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('address', models.TextField(max_length=200)),
                ('phone', models.IntegerField(max_length=200)),
            ],
        ),
    ]
