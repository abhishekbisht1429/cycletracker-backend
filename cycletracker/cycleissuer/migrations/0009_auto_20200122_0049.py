# Generated by Django 3.0.2 on 2020-01-22 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cycleissuer', '0008_auto_20200122_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
