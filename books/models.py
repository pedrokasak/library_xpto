from django.conf import settings
from django.db import models




class Authors(models.Model):
    name = models.CharField(verbose_name='Nome do Autor', max_length=60)
    
    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

class Books(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, null=True, blank=True)
    
    name = models.CharField(verbose_name='Nome do Livro', max_length=60)
    create_by = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    publishing_company = models.CharField(verbose_name='Editora', max_length=60)
    authors = models.ForeignKey(Authors, verbose_name='Autor', on_delete=models.CASCADE)
    
    
    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name
