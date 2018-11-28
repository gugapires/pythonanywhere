from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True) # Esse "unique" significa que eu posso usar como chave primaria

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

# Atenção : the field category in model Page is of type ForeignKey

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

# Estou no livro pag. 51

