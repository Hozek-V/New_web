from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=255)
    # author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=30)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.title} {self.isbn}"
