# Generated by Django 4.2.3 on 2023-08-15 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addTask', '0002_remove_addtask_id_alter_addtask_duedate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addtask',
            name='task_id',
        ),
        migrations.AddField(
            model_name='addtask',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]