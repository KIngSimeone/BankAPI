# Generated by Django 3.1.1 on 2020-09-15 17:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.TextField(verbose_name='first_name')),
                ('lastName', models.TextField(verbose_name='last_name')),
                ('userName', models.TextField(verbose_name='user_name')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.TextField()),
                ('phone', models.TextField()),
                ('isDeleted', models.BooleanField(default=False, verbose_name='is_deleted')),
                ('createdAt', models.DateField(auto_now_add=True, verbose_name='created_at')),
                ('updatedAt', models.DateField(auto_now=True, verbose_name='updated_at')),
                ('isActive', models.BooleanField(default=True, verbose_name='is_active')),
                ('lastActiveOn', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last_active_on')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='UserPasswordResetTokens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resetToken', models.TextField(verbose_name='rest_token')),
                ('expires_at', models.DateField(verbose_name='expires_at')),
                ('createdAt', models.DateField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='updated_at')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserAccessTokens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accessToken', models.TextField(verbose_name='access_token')),
                ('expiresAt', models.DateTimeField(verbose_name='expires_at')),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updatedAt', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.user')),
            ],
            options={
                'verbose_name': 'User Access Token',
                'verbose_name_plural': 'User Access Tokens',
            },
        ),
        migrations.CreateModel(
            name='HomeAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.TextField()),
                ('city', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=64)),
                ('country', models.CharField(max_length=64)),
                ('zipCode', models.CharField(max_length=64)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.user')),
            ],
        ),
    ]