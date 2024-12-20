# Generated by Django 4.2.16 on 2024-11-16 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation_system', '0002_alter_rooms_equipments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('capacity', models.IntegerField()),
                ('equipments', models.ManyToManyField(blank=True, related_name='rooms', to='reservation_system.equipment')),
            ],
        ),
        migrations.DeleteModel(
            name='Rooms',
        ),
        migrations.AddField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='reservation_system.room'),
        ),
        migrations.AlterUniqueTogether(
            name='reservation',
            unique_together={('room', 'date')},
        ),
    ]
