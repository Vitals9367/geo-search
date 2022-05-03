# Generated by Django 3.2.12 on 2022-05-03 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("address", "0004_add_postal_code_area"),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="municipality",
            field=models.ForeignKey(
                default="helsinki",
                on_delete=django.db.models.deletion.CASCADE,
                to="address.municipality",
            ),
            preserve_default=False,
        ),
    ]
