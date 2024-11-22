# Generated by Django 4.2.15 on 2024-11-22 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sucursal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_name', models.CharField(max_length=100)),
                ('employee_surname', models.CharField(max_length=100)),
                ('employee_hire_date', models.DateField()),
                ('employee_DNI', models.CharField(max_length=20, unique=True)),
                ('branch_id', models.ForeignKey(db_column='branch_id', on_delete=django.db.models.deletion.CASCADE, to='sucursal.sucursal')),
            ],
        ),
    ]
