# Generated by Django 3.0.7 on 2020-08-07 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
    ]
