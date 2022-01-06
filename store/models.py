from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "categories"
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='uploads')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    quantity_left = models.IntegerField()
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
