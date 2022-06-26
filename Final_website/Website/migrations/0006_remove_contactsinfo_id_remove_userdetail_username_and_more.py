# Generated by Django 4.0.4 on 2022-04-30 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0005_rename_userdetails_userdetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactsinfo',
            name='id',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='Username',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='id',
        ),
        migrations.AddField(
            model_name='userdetail',
            name='username',
            field=models.CharField(default='No User', max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='contactsinfo',
            name='email',
            field=models.EmailField(max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='email',
            field=models.EmailField(max_length=200, unique=True),
        ),
    ]
