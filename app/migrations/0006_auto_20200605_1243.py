# Generated by Django 3.0.6 on 2020-06-05 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200605_1229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction_history',
            old_name='Rec',
            new_name='Reciever',
        ),
        migrations.AddField(
            model_name='transaction_history',
            name='Reciever_Credit',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='transaction_history',
            name='Sender_Credit',
            field=models.IntegerField(null=True),
        ),
    ]
