# Generated by Django 4.0.5 on 2022-06-10 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_alter_photo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(default=True, upload_to='images'),
            preserve_default=False,
        ),
    ]
