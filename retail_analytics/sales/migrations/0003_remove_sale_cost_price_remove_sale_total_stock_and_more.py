# Generated by Django 5.2.3 on 2025-07-18 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_sale_cost_price_sale_total_stock_alter_sale_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='cost_price',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='total_stock',
        ),
        migrations.AlterField(
            model_name='sale',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='sale',
            name='discount',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='sale',
            name='selling_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='sale',
            name='total_revenue',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]
