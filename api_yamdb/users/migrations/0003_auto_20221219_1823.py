# Generated by Django 3.2 on 2022-12-19 15:23

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20221213_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'User'), ('admin', 'Admin'), ('moderator', 'Moderator')], default='user', max_length=50, verbose_name='Роль'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True, validators=[users.validators.validate_username], verbose_name='Имя пользователя'),
        ),
    ]
