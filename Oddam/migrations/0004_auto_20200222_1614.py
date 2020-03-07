# Generated by Django 2.2.6 on 2020-02-22 15:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Oddam", "0003_donation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="institution",
            name="type",
            field=models.CharField(
                choices=[
                    ("ORG", "Organizacja pozarządowa"),
                    ("FUND", "Fundacja"),
                    ("GAT", "Zbiórka lokalna"),
                ],
                default="FUND",
                max_length=4,
            ),
        ),
    ]
