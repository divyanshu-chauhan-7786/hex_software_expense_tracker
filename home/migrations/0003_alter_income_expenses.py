# Generated by Django 5.1.1 on 2024-09-21 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_income_expenses_alter_income_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='expenses',
            field=models.FloatField(default=0),
        ),
    ]
