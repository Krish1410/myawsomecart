# Generated by Django 3.1 on 2022-08-21 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20220817_0858'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contect',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('desc', models.CharField(max_length=1000)),
            ],
        ),
    ]