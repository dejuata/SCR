from django.core.serializers.json import DjangoJSONEncoder

from ..ruta.models import Ruta
from ..conductor.models import Conductor
from ..vehiculo.models import Vehiculo

import json


def ruta_json():
    return json.dumps(list(Ruta.objects.values('codigo_ruta',
                                               'nombre_ruta',
                                               'hora_inicio',
                                               'hora_fin',
                                               'valor_hora_adicional',
                                               'kilometros',
                                               'valor_ruta',
                                               'valor_tercero',
                                               )), cls=DjangoJSONEncoder)


def conductor_json():
    return json.dumps(list(Conductor.objects.values('cedula',
                                                    'apellidos',
                                                    'nombres',
                                                    ).order_by('apellidos')))


def vehiculo_json():
    return json.dumps(list(Vehiculo.objects.values('placa')))
