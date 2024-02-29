# Generated by Django 5.0.2 on 2024-02-28 16:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_reservation_customer_email_reservation_customer_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='IceReservationStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ice_status', models.CharField(max_length=100)),
                ('description_ice', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='status',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='customer_email',
            new_name='ice_customer_email',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='customer_name',
            new_name='ice_customer_name',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='time_slot',
        ),
        migrations.AddField(
            model_name='reservation',
            name='ice_customer',
            field=models.CharField(default='No User', max_length=100),
        ),
        migrations.AddField(
            model_name='reservation',
            name='ice_time_slot',
            field=models.CharField(default='Not Provided', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='ice_status',
            field=models.ForeignKey(default= 1, on_delete=django.db.models.deletion.CASCADE, to='reservation.icereservationstatus'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ReservationStatus',
        ),
    ]