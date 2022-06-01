# Generated by Django 4.0.4 on 2022-05-31 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('cpf', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('role', models.CharField(choices=[('1', 'Gerente de Departamento'), ('2', 'Gerente de Empresa'), ('3', 'Funcionário')], max_length=100, verbose_name='Cargo')),
                ('allowance', models.BooleanField(default=False, verbose_name='Abono')),
                ('name', models.CharField(max_length=100)),
                ('telephone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('wage', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprisems.department')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='enterprisems.person')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprisems.company')),
            ],
            bases=('enterprisems.person',),
        ),
        migrations.CreateModel(
            name='DepartmentManager',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='enterprisems.person')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprisems.department')),
            ],
            bases=('enterprisems.person',),
        ),
        migrations.CreateModel(
            name='CompanyManager',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='enterprisems.person')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprisems.company')),
            ],
            bases=('enterprisems.person',),
        ),
    ]
