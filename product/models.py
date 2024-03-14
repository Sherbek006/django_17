from django.db import models

# Create your models here.
class Product(models.Model):
    category_id = models.ForeignKey('Category',on_delete = models.CASCADE)
    title = models.CharField(max_length=300)
    image =  models.ImageField(upload_to='images')
    description = models.TextField()
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)
    
    def __str__(self):
        return self.title
    
class Category(models.Model):
    title = models.CharField(max_length = 100)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)
    
    def __str__(self) -> str:
        return self.title

    
    

