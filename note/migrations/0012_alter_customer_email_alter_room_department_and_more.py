# Generated by Django 4.1.4 on 2023-07-20 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0011_alter_customer_email_alter_room_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name='room',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='note.departments'),
        ),
        migrations.AlterField(
            model_name='room',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='note.semester'),
        ),
    ]