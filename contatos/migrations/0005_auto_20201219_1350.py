# Generated by Django 3.1.4 on 2020-12-19 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0004_contato_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%m'),
        ),
    ]