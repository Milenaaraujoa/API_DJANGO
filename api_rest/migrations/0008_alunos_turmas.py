# Generated by Django 5.1.4 on 2025-02-06 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0007_remove_alunos_turmas'),
    ]

    operations = [
        migrations.AddField(
            model_name='alunos',
            name='turmas',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
