from django.db import models

# Criar tabela
class pokemon(models.Model):
    number = models.TextField(max_length=3)
    name = models.TextField(max_length=50)
    image = models.ImageField(upload_to="pokemon/static/imagens")
    image_name = models.TextField(max_length=50, default= None)
    type1 = models.TextField(max_length=20)
    type2 = models.TextField(max_length=20)
    raridade = models.TextField(max_length=10, default="comun")

    # Colocar como nome do objeto o campo name
    def __str__(self):
        return self.name

class Meta:
    ordering = ('number',)
