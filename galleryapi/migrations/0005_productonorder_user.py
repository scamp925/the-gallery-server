# Generated by Django 4.1.5 on 2023-01-24 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galleryapi', '0004_alter_productonorder_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='productonorder',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='galleryapi.user'),
            preserve_default=False,
        ),
    ]