import uuid
from django.db import models
from .base import Base
from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Peao(Base):
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width':480, 'height': 480, 'crop':True}})
    descricao = models.CharField('Descrição', max_length=100)

    class Meta:
        verbose_name = 'Peão'
        verbose_name_plural = 'Peões'

    def __str__(self):
        return str(self.descricao)