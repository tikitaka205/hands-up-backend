# Generated by Django 4.1.3 on 2022-12-19 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "phone",
                    models.CharField(max_length=15, unique=True, verbose_name="phone"),
                ),
                (
                    "username",
                    models.CharField(
                        max_length=128, unique=True, verbose_name="username"
                    ),
                ),
                (
                    "profile_image",
                    models.ImageField(
                        blank=True, default="default.jpeg", upload_to="media"
                    ),
                ),
                ("kakao_id", models.CharField(blank=True, max_length=100)),
                ("rating_score", models.SmallIntegerField(default=40)),
                ("temp_score", models.SmallIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
                ("react_at", models.CharField(blank=True, max_length=12, null=True)),
            ],
            options={
                "db_table": "User",
            },
        ),
        migrations.CreateModel(
            name="AuthSms",
            fields=[
                (
                    "phone_number",
                    models.CharField(
                        max_length=11,
                        primary_key=True,
                        serialize=False,
                        verbose_name="휴대폰 번호",
                    ),
                ),
                ("auth_number", models.IntegerField(verbose_name="인증 번호")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "AuthSms",
            },
        ),
    ]
