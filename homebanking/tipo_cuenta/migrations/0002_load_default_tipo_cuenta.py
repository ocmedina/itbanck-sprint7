from django.db import migrations

def load_tipo_cuenta(apps, schema_editor):
    TipoCuenta = apps.get_model('tipo_cuenta', 'TipoCuenta')
    TipoCuenta.objects.bulk_create([
        TipoCuenta(id=1, nombre='Caja de ahorro en pesos'),
        TipoCuenta(id=2, nombre='Caja de ahorro en dólares'),
        TipoCuenta(id=3, nombre='Cuenta corriente'),
    ])

class Migration(migrations.Migration):
    dependencies = [
        ('tipo_cuenta', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_tipo_cuenta),
    ]
