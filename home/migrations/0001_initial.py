# Generated by Django 4.1 on 2022-08-22 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.EmailField(max_length=50)),
                ('address', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=13)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=50)),
                ('pin', models.CharField(max_length=10)),
                ('date', models.DateField()),
            ],
        ),
    ]
