# Generated by Django 4.0.5 on 2022-07-02 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0003_agendamento_hora_agendada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='data_agendada',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='data_registro',
            field=models.DateTimeField(default='02-07-2022 04:05:46'),
        ),
    ]
