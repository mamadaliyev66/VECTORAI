# Generated by Django 4.2.4 on 2023-08-06 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_delete_teammembers'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title', models.CharField(max_length=255)),
                ('text', models.TextField(max_length=300)),
                ('location', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=50)),
                ('email_address', models.CharField(max_length=50)),
            ],
        ),
    ]
