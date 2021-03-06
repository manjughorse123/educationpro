# Generated by Django 4.0 on 2021-12-30 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_delete_userrole'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('Code', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MajorProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('session_rate', models.FloatField(default=0.0)),
                ('teach_curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_curriculum', to='teacher.curriculum')),
                ('teach_education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_education', to='teacher.education')),
                ('teach_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_prefered_subject', to='teacher.subject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_sub_id', to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('about', models.TextField(blank=True, null=True)),
                ('teaching_experience', models.CharField(max_length=20)),
                ('teaching_description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('teach_degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_degree', to='teacher.degree')),
                ('teach_language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_language', to='teacher.language')),
                ('teach_major_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_major_project', to='teacher.majorproject')),
                ('teach_university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_university', to='teacher.university')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_teacher', to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='TeachAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(blank=True, max_length=20, null=True)),
                ('hour', models.TimeField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_availability', to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='BilingInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(blank=True, max_length=20, null=True)),
                ('iban', models.CharField(blank=True, max_length=20, null=True)),
                ('account_owner_name', models.CharField(blank=True, max_length=20, null=True)),
                ('Account_number', models.IntegerField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='biling_currency', to='teacher.currency')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_teacher', to='user.user')),
            ],
        ),
    ]
