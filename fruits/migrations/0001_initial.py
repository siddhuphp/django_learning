# Generated by Django 3.0.3 on 2020-02-25 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fruits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fruit_name', models.CharField(max_length=20)),
                ('cost', models.CharField(max_length=20)),
                ('quanty', models.CharField(max_length=10)),
            ],
        ),
    ]
