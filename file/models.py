from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    """
    Represents a category for files in the application.
    """
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class File(models.Model):
    """
    Represents a file(book) for sale in the application.
    """
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_year = models.PositiveIntegerField()
    category = models.ForeignKey(Category, related_name='files', on_delete=models.CASCADE)
    language = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    available = models.BooleanField(default=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    num_ratings = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='file_images', blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='uploaded_files', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    file_type = models.CharField(max_length=50, choices=[('pdf', 'PDF'), ('slides', 'Slides'), ('doc', 'Doc')])
    file = models.FileField(upload_to='docs/')

    def __str__(self):
        return self.title


class Payment(models.Model):
    """
    Represents payment for the file/doc(BOOK) to be downloaded
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
