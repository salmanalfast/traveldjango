# Generated by Django 3.2 on 2022-09-26 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listmenu', '0002_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='imagedb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.BinaryField()),
            ],
        ),
    ]
