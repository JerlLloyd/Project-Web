# Generated by Django 4.2.9 on 2024-03-07 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_product_orderitem_product_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='m_description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='m_keyword',
        ),
        migrations.RemoveField(
            model_name='category',
            name='m_title',
        ),
        migrations.RemoveField(
            model_name='product',
            name='m_description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='m_keyword',
        ),
        migrations.RemoveField(
            model_name='product',
            name='m_title',
        ),
    ]
