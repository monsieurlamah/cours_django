from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    # post = models.ManyToManyField(Post)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name