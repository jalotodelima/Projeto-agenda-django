from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# id (primary key - automático)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)

# Depois
# category (foreign key), show (boolean), owner (foreign key)
# picture (imagem)


class Category(models.Model):
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(
        max_length=50, help_text="Insira seu primeiro nome")
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m/', blank=True)
    category = models.ForeignKey(
        Category,
        # quando apagar a categoria, fica nulo no nome da categoria no contato
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    owner = models.ForeignKey(
        User,
        # quando apagar a categoria, fica nulo no nome da categoria no contato
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    # colocar o nome lá na base de dados (antes ficaria "contact object (1 ou ID que fosse)")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
