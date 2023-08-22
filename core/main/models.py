from django.db import models

# Create your models here.




class Category(models.Model):
    name = models.CharField('Category name',max_length=60)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    title = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='cat_prod')
    name = models.CharField('Product name',max_length=60)
    price = models.PositiveIntegerField('Product price')
    img = models.ImageField('Product images',upload_to='main_images')
    
    def __str__(self):
        return self.name
    