from django.contrib import admin
from django.contrib.admin import ModelAdmin
# Register your models here.

from .models import Contacto
from .models import Usuarios
from .models import Medidas
from .models import Opotunidades
from .models import Indicadores
from .models import Basculas
from .models import Tecnologias
from .models import Planos
from .models import Obras_civiles
from .models import Industrias
from .models import Ubicaciones
from .models import Empresas
from .models import Registros_fotograficos
from .models import Configuraciones




admin.site.register(Usuarios, ModelAdmin)
admin.site.register(Contacto)
admin.site.register(Medidas)
admin.site.register(Opotunidades)
admin.site.register(Indicadores)
admin.site.register(Basculas)
admin.site.register(Tecnologias)
admin.site.register(Planos)
admin.site.register(Obras_civiles)
admin.site.register(Industrias)
admin.site.register(Ubicaciones)
admin.site.register(Empresas)
admin.site.register(Registros_fotograficos)
admin.site.register(Configuraciones)







