# Generated by Django 3.2.5 on 2021-07-09 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200, verbose_name='Nome')),
                ('lastname', models.CharField(max_length=200, verbose_name='Sobrenome')),
                ('admisson_date', models.DateField(verbose_name='Data de Admissão')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='scheduleApp.doctor')),
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='scheduleApp.place')),
            ],
        ),
        migrations.CreateModel(
            name='Day_Of',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of', models.CharField(choices=[('seg', 'Segunda'), ('ter', 'Terça'), ('qua', 'Quarta'), ('qui', 'Quinta'), ('sex', 'Sexta'), ('sab', 'Sabado'), ('dom', 'Domingo')], max_length=15, verbose_name='Dia de folga')),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='scheduleApp.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=200, verbose_name='País')),
                ('state', models.CharField(max_length=200, verbose_name='Estado')),
                ('city', models.CharField(max_length=200, verbose_name='Cidade')),
                ('district', models.CharField(max_length=200, verbose_name='Bairro')),
                ('street', models.CharField(max_length=200, verbose_name='Rua')),
                ('number', models.IntegerField(verbose_name='Numero')),
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='scheduleApp.place')),
            ],
        ),
    ]
