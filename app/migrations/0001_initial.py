# Generated by Django 2.2.5 on 2019-10-11 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Circle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('rank', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=60)),
                ('points', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=60)),
                ('points', models.IntegerField()),
                ('circles', models.ManyToManyField(to='app.Circle')),
                ('posts', models.ManyToManyField(to='app.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Replay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=60)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student')),
                ('post_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student'),
        ),
        migrations.AddField(
            model_name='post',
            name='circle_entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Circle'),
        ),
        migrations.AddField(
            model_name='post',
            name='replays',
            field=models.ManyToManyField(to='app.Replay'),
        ),
        migrations.AddField(
            model_name='circle',
            name='posts',
            field=models.ManyToManyField(to='app.Post'),
        ),
        migrations.AddField(
            model_name='circle',
            name='students',
            field=models.ManyToManyField(to='app.Student'),
        ),
    ]