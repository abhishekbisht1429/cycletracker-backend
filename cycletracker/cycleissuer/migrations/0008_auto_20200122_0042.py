# Generated by Django 3.0.2 on 2020-01-22 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cycleissuer', '0007_user_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='branch',
            field=models.CharField(max_length=100),
        ),
    ]
