from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Category Name")
    slug = models.CharField(max_length=255, unique=True, verbose_name="Category Slug")
    description = RichTextField(blank=True, null=True, verbose_name="Description")
    icon = models.ImageField(upload_to="category_icons", blank=True, null=True)
    image = models.ImageField(upload_to="category_images", blank=True, null=True, verbose_name="Category Image")
    is_active = models.BooleanField(default=True, verbose_name="Status")
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ('name',)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class CategorySection(models.Model):
    category = models.ForeignKey(Category, related_name="category_section", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="Category Section Name")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ('name',)
        verbose_name = "category section"
        verbose_name_plural = "category sections"

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name="sub_category", on_delete=models.CASCADE)
    section = models.ForeignKey(CategorySection, related_name="sec_sub_category", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="Subcategory Name")
    slug = models.CharField(max_length=255, unique=True, verbose_name="Subcategory Slug")
    description = RichTextField(blank=True, null=True, verbose_name="Description")
    is_active = models.BooleanField(default=True, verbose_name="status")
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ('name',)
        verbose_name = "subcategory"
        verbose_name_plural = "subcategories"

    def __str__(self):
        return self.name


class Upload(models.Model):
    upload_image = models.ImageField(upload_to="uploads")


