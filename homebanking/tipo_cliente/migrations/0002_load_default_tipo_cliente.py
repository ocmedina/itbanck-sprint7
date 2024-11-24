from django.db import migrations

def load_tipo_cliente(apps, schema_editor):
    TipoCliente = apps.get_model('tipo_cliente', 'TipoCliente')
    TipoCliente.objects.bulk_create([
        TipoCliente(id=1, nombre='Classic'),
        TipoCliente(id=2, nombre='Gold'),
        TipoCliente(id=3, nombre='Black'),
    ])

class Migration(migrations.Migration):
    dependencies = [
        ('tipo_cliente', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_tipo_cliente),
    ]
