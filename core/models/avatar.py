import uuid
from django.db import models
from .base import Base
from stdimage.models import StdImageField

#import relacionamentos
from django.contrib.auth.models import User

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Avatar(Base):
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width':480, 'height': 480, 'crop':True}})
    descricao = models.CharField('Descrição', max_length=100)
    usuario = models.ManyToManyField(User, related_name='UsuarioAvatar', through='UsuarioAvatar')

    class Meta:
        verbose_name = 'Avatar'
        verbose_name_plural = 'Avatares'

    def __str__(self):
        return str(self.descricao)

class UsuarioAvatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='avatar_usuario', unique=True)
    avatar = models.ForeignKey(Avatar, on_delete=models.CASCADE, related_name='avatar_usuario')

    class Meta:
        verbose_name = 'Usuario Avatar'

    def __str__(self):
        return str(self.pk)
