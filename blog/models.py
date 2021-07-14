from django.db import models
from django.utils.text import slugify
from django.utils.html import strip_tags
from PIL import Image as PILImage
from tinymce.models import HTMLField
from tinymce import models as tinymce_models


class Article(models.Model):
    published_status_choices = (
        ('draft', 'Draft'),
        ('pending_review', 'Pending Review'),
        ('published', 'Published'),
    )

    author = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    short_description = tinymce_models.HTMLField('short_description')
    content = tinymce_models.HTMLField('Content')
    tag = models.ManyToManyField('Tag', related_name='article', blank=True)
    category = models.ForeignKey('Category', related_name='article', on_delete=models.CASCADE, blank=True, null=True)
    # img = models.ForeignKey(Image, related_name='blog', on_delete=models.CASCADE, blank=True, null=True)
    published_status = models.CharField(max_length=30, choices=published_status_choices)
    visibility = models.BooleanField(default=True)
    date_published = models.DateField(auto_now=False, auto_now_add=False)

    is_featured = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, blank=True, null=True, unique=True)

    def save(self, *args, **kwargs):
        if self.title and not self.slug:
            stripped = strip_tags(self.title)
            remove_p = stripped[1:-1]
            self.slug = slugify(remove_p)
        super(type(self), self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.category} - {self.slug} -- {self.date_published}'


class Comment(models.Model):
    comment = models.ForeignKey(Article, related_name='comment', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    author = models.CharField(max_length=50, blank=True, null=True)
    text = models.CharField(max_length=255, blank=True, null=True)
    parent_comment = models.ForeignKey('self', related_name='child_comment', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment dated: {self.date} -- Approved: {self.approved}'


class Category(models.Model):
    name = models.CharField(max_length=75, blank=True, null=True, unique=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.name and not self.slug:
            self.slug = slugify(self.name)
        super(type(self), self).save(*args, **kwargs)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=75, blank=True, null=True, unique=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.name and not self.slug:
            self.slug = slugify(self.name)
        super(type(self), self).save(*args, **kwargs)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name