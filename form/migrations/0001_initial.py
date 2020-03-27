# Generated by Django 3.0.4 on 2020-03-26 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CovidModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('question1', models.CharField(max_length=5)),
                ('question2', models.CharField(max_length=5)),
                ('question3', models.CharField(max_length=5)),
                ('question4', models.CharField(max_length=5)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
