# Generated by Django 4.1.3 on 2024-09-22 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
