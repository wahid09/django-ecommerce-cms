# Generated by Django 4.1.1 on 2022-10-02 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("category", "0004_rename_image_upload_upload_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="category", old_name="icon", new_name="category_icon",
        ),
        migrations.RenameField(
            model_name="category", old_name="image", new_name="category_image",
        ),
    ]
