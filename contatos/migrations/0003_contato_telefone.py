# Generated by Django 3.1.4 on 2020-12-19 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0002_contato_mostrar'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='telefone',
            field=models.CharField(default=1111111, max_length=255),
            preserve_default=False,
        ),
    ]
