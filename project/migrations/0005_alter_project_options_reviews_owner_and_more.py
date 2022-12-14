# Generated by Django 4.0.6 on 2022-08-08 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_rename_decription_skill_description'),
        ('project', '0004_project_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='reviews',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.profile'),
        ),
        migrations.AlterUniqueTogether(
            name='reviews',
            unique_together={('owner', 'project')},
        ),
    ]
