# Generated by Django 3.2.7 on 2021-09-26 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExlData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.TextField(null=True)),
                ('fare', models.TextField(null=True)),
                ('name', models.TextField(null=True)),
            ],
        ),
    ]