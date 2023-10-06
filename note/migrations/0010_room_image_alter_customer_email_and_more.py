# Generated by Django 4.1.4 on 2023-07-20 16:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0009_orderitem_shippingaddress_remove_cartproduct_cart_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='image',
            field=models.ImageField(default='avatar.svg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(null=True,blank=True, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='department',
            field=models.ForeignKey(null=True,blank=True, on_delete=django.db.models.deletion.CASCADE, to='note.departments'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='semester',
            field=models.ForeignKey(null=True,blank=True, on_delete=django.db.models.deletion.CASCADE, to='note.semester'),
            preserve_default=False,
        ),
    ]