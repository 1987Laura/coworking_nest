from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('deskdrop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.DateField(default='2025-09-21'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='start_time',
            field=models.TimeField(default='09:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='hours_reserved',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
