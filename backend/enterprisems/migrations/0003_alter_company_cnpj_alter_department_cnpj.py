# Generated by Django 4.0.5 on 2022-07-08 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprisems', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='cnpj',
            field=models.CharField(max_length=14, null=True, unique=True, verbose_name='CNPJ'),
        ),
        migrations.AlterField(
            model_name='department',
            name='cnpj',
            field=models.CharField(max_length=14, null=True, unique=True, verbose_name='CNPJ'),
        ),
    ]
