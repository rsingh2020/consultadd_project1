# Generated by Django 3.0.5 on 2020-04-28 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=30)),
                ('Last_name', models.CharField(max_length=30)),
                ('Email_Id', models.CharField(max_length=30)),
                ('Contact', models.CharField(max_length=30)),
                ('Address', models.CharField(max_length=30)),
            ],
        ),
    ]
