# Generated by Django 2.0.8 on 2018-09-25 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_ticket_data_criacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('1', 'novo'), ('2', 'resolvido'), ('3', 'em progresso')], default='1', max_length=1, null=True),
        ),
    ]
