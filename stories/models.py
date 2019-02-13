from django.db import models


class Story(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "stories"
