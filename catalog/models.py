from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:category', kwargs={'slug': self.slug})
    

class Author(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['name']

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField('Título', max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Autor')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Categoria')
    slug = models.SlugField('Identificador', max_length=255)
    publication_date = models.DateField('Data de publicação')
    cover_image = models.URLField()
    price = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    synopsis = models.TextField('Sinópsi')
    number_of_pages = models.IntegerField('Número de páginas')
    publisher = models.CharField('Editora', max_length=100)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('catalog:book', kwargs={'slug': self.slug})
