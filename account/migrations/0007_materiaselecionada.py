# Gerado pelo Django 4.0.3 em 2023-12-03 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_delete_materia_delete_turma'),
    ]

    operations = [
        # Criação do Modelo 'MateriaSelecionada'
        migrations.CreateModel(
            name='MateriaSelecionada',
            fields=[
                ('idTurmaProfessor', models.IntegerField(primary_key=True, serialize=False)),
                ('nomeProfessor', models.CharField(max_length=255)),
                ('numeroTurma', models.IntegerField()),
                ('horario', models.CharField(max_length=10)),
                ('carga', models.CharField(max_length=5)),
                ('idmateria', models.IntegerField()),
                ('codMateria', models.CharField(max_length=10)),
                ('nomeMateria', models.CharField(max_length=255)),
                ('curso', models.CharField(max_length=50)),
                ('curso2', models.CharField(blank=True, max_length=50)),
                ('curso3', models.CharField(blank=True, max_length=50)),
                ('curso4', models.CharField(blank=True, max_length=50)),
                ('curso5', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]