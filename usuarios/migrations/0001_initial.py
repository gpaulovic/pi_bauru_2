# Generated by Django 4.2.4 on 2023-09-01 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ecopontos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='-', max_length=30)),
                ('cpf', models.CharField(default='-', max_length=15)),
                ('email', models.CharField(default='-', max_length=30)),
                ('cargo', models.CharField(default='-', max_length=30)),
                ('ecoponto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecopontos.ecopontos')),
            ],
        ),
    ]
