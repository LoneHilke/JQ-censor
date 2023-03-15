# Generated by Django 4.1.7 on 2023-03-14 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fag', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Klassetrin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('klasse', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Censor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('fag', models.ManyToManyField(related_name='item', to='censor.fag')),
                ('klassetrin', models.ManyToManyField(related_name='item', to='censor.klassetrin')),
                ('teacher', models.ManyToManyField(related_name='item', to='censor.teacher')),
            ],
        ),
    ]