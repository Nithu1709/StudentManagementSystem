import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('course', models.CharField(
                    choices=[
                        ('CSE', 'Computer Science & Engineering'),
                        ('ECE', 'Electronics & Communication'),
                        ('MECH', 'Mechanical Engineering'),
                        ('CIVIL', 'Civil Engineering'),
                        ('IT', 'Information Technology'),
                        ('MBA', 'Business Administration'),
                        ('OTHER', 'Other'),
                    ],
                    default='OTHER',
                    max_length=10,
                )),
                ('enrollment_date', models.DateField()),
                ('gpa', models.DecimalField(
                    decimal_places=2,
                    default=0.0,
                    max_digits=3,
                    validators=[
                        django.core.validators.MinValueValidator(0.0),
                        django.core.validators.MaxValueValidator(10.0),
                    ],
                )),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
    ]
