# Generated by Django 2.2.6 on 2020-02-19 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Oddam", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Institution",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("description", models.CharField(max_length=252)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("ORG", "Organizacja pozarządowa"),
                            ("FUND", "Fundacja"),
                            ("GAT", "Zbiórka lokalna"),
                        ],
                        default="FUND",
                        max_length=3,
                    ),
                ),
                ("categories", models.ManyToManyField(to="Oddam.Category")),
            ],
        ),
    ]
