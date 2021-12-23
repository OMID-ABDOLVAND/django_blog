from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
# Create your models here.


class Category(models.Model):
    title = models.CharField(verbose_name=_("title"), max_length=225)
    active = models.BooleanField(verbose_name=_("active"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class Post(models.Model):
    class StatusChoices(models.TextChoices):
        DRAFT = _("draft")
        PUBLISHED = _("published")
    title = models.CharField(verbose_name=_("title"))
    slug = models.SlugField(verbose_name=_("slug"), allow_unicode=True, null=False, unique_for_date="publish_time")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    lead = models.CharField(verbose_name=_("lead"), max_length=1024, null=True, blank=True)
    body = models.TextField(verbose_name=_("body"))
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    created = models.DateField(verbose_name=_("created"), auto_now_add=True)
    updated = models.DateField(verbose_name=_("updated"), auto_now=True)

    status = models.CharField(verbose_name=_("status"), max_length=15, choices=StatusChoices.choices,
                              default=StatusChoices.DRAFT)  # line 7 8 9 32 33

    publish_time = models.DateField(verbose_name=_("publish time"), null=True, blank=True)

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")
        ordering = ['-publish_time']
