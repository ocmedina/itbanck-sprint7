from django.db import migrations

def load_marcas(apps, schema_editor):
    MarcaTarjeta = apps.get_model('marca_tarjeta', 'MarcaTarjeta')
    MarcaTarjeta.objects.bulk_create([
        MarcaTarjeta(id=1, nombre='Visa'),
        MarcaTarjeta(id=2, nombre='MasterCard'),
        MarcaTarjeta(id=3, nombre='Amex'),
    ])

class Migration(migrations.Migration):
    dependencies = [
        ('marca_tarjeta', '0001_initial'), 
    ]

    operations = [
        migrations.RunPython(load_marcas),
    ]
