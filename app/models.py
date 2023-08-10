from typing import Iterable, Optional
from django.db import models



class Category (models.Model) :
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self) :
        return f'{self.name}'

class Book (models.Model) : 
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    book = models.FileField(upload_to='books/',max_length=1000000)

    def __str__(self) : 
        return f'{self.name} -> {self.category}'
    
