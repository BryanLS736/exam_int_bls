# Generated by Django 5.1.3 on 2024-12-01 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comensal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=35)),
                ('apellido', models.CharField(max_length=40)),
                ('dni', models.CharField(default='00000000', max_length=8)),
            ],
        ),
    ]
