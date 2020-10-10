# Generated by Django 3.1.2 on 2020-10-05 01:20

import dining_hall.accounts.managers
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id do usuário')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='nome de usuário')),
                ('name', models.CharField(max_length=255, verbose_name='nome')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='e-mail')),
                ('entry_date', models.DateField(blank=True, null=True, verbose_name='data de ingresso')),
                ('is_active', models.BooleanField(default=True, verbose_name='ativo')),
                ('is_staff', models.BooleanField(default=False, verbose_name='equipe')),
                ('is_admin', models.BooleanField(default=False, verbose_name='administrador')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'usuário',
                'verbose_name_plural': 'usuários',
            },
            managers=[
                ('objects', dining_hall.accounts.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Servant',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.user')),
            ],
            options={
                'verbose_name': 'servidor',
                'verbose_name_plural': 'servidores',
            },
            bases=('accounts.user',),
            managers=[
                ('objects', dining_hall.accounts.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.user')),
                ('birthdate', models.DateField(verbose_name='data de nascimento')),
                ('cpf', models.CharField(max_length=15, unique=True, verbose_name='CPF')),
                ('rg', models.CharField(max_length=20, unique=True, verbose_name='RG')),
                ('phone', models.CharField(max_length=14, unique=True, verbose_name='telefone')),
                ('profilepic', models.ImageField(blank=True, null=True, upload_to='', verbose_name='foto')),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='course.class', verbose_name='turma')),
            ],
            options={
                'verbose_name': 'aluno',
                'verbose_name_plural': 'alunos',
            },
            bases=('accounts.user',),
            managers=[
                ('objects', dining_hall.accounts.managers.UserManager()),
            ],
        ),
    ]