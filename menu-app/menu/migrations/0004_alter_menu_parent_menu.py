# Generated by Django 3.2 on 2023-03-03 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_rename_menu_id_menu_parent_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='parent_menu',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
