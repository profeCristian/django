# Generated by Django 3.1.1 on 2022-05-24 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id_genero', models.AutoField(db_column='idGenero', primary_key=True, serialize=False)),
                ('genero', models.CharField(max_length=20)),
            ],
        ),
    ]
