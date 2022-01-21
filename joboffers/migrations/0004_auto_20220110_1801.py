# Generated by Django 3.2.9 on 2022-01-10 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pycompanies', '0003_usercompanyprofile'),
        ('joboffers', '0003_auto_20211125_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joboffer',
            name='company',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pycompanies.company', verbose_name='Empresa'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='contact_mail',
            field=models.EmailField(blank=True, max_length=255, null=True, verbose_name='Correo electrónico'),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='state',
            field=models.CharField(choices=[('NEW', 'Nuevo'), ('DEACTIVATED', 'Desactivada'), ('MODERATION', 'En moderación'), ('ACTIVE', 'Activa'), ('REJECTED', 'Rechazada'), ('EXPIRED', 'Caducada')], default='DEACTIVATED', max_length=32, verbose_name='Estado de la oferta'),
        ),
    ]