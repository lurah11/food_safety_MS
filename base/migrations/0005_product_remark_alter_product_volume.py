# Generated by Django 4.2.8 on 2023-12-13 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='remark',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='volume',
            field=models.CharField(max_length=100),
        ),
    ]