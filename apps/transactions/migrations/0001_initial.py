# Generated by Django 2.2.5 on 2019-09-26 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dates', models.DateTimeField(default=False)),
                ('types', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('description', models.TextField()),
                ('invetory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='inventories.Inventory')),
            ],
            options={
                'db_table': 'transactions',
            },
        ),
    ]
