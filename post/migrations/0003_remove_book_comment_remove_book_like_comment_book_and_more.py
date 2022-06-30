# Generated by Django 4.0.5 on 2022-06-30 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_book_comment_alter_book_like_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='book',
            name='like',
        ),
        migrations.AddField(
            model_name='comment',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.book'),
        ),
        migrations.AddField(
            model_name='like',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.book'),
        ),
    ]
