# Generated by Django 4.0.4 on 2022-05-04 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0007_alter_userdetail_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='billInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Items', models.CharField(max_length=100)),
                ('total', models.IntegerField()),
            ],
        ),
    ]