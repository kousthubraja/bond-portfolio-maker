# Generated by Django 3.0.3 on 2020-02-03 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isin', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('ytm', models.FloatField(default=0)),
                ('tenor', models.IntegerField(default=10)),
            ],
        ),
    ]
