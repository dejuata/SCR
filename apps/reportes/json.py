from ..ruta.models import Ruta
from ..conductor.models import Conductor
from ..cliente.models import Cliente
from ..vehiculo.models import Vehiculo
from ..planilla.models import Planilla

from datetime import date

import json


def total_clientes():
    return Cliente.objects.count()


def total_rutas():
    return Ruta.objects.count()


def total_conductores():
    return Conductor.objects.count()


def lic_vencida_conductores():
    return Conductor.objects.filter(estado_licencia=False).count()


def total_vehiculos():
    return Vehiculo.objects.count()


def to_vencida_vehiculos():
    vehiculos = Vehiculo.objects.all()
    count = 0

    for vehiculo in vehiculos:
        if vehiculo.fecha_vencimiento_tarjeta_operacion < date.today():
            count += 1

    return count


def horas_laboradas_por_conductor():
    return json.dumps(list(Planilla.objects.values('conductor',
                                                   'tiempo_operado',
                                                   'adicional_conductor',
                                                   'flota')))


def reporte_horas_laboradas_por_conductor():
    conductor_array = []
    tiempo_operado_array = []
    tiempo_operado = []
    planilla = Planilla.objects.values('conductor', 'tiempo_operado')

    # Lleno un arreglo con el id de los conductores y el tiempo_operado
    for value in planilla:
        conductor_array.append(value.get('conductor'))
        tiempo_operado_array.append(value.get('tiempo_operado'))

    # Elimino valores duplicados
    conductor = list(set(conductor_array))

    # Inicializo el arreglo con cero
    for i in range(len(conductor)):
        tiempo_operado.append(0)

    # Realizo sumatoria
    for i in range(len(conductor)):
        for j in range(len(conductor_array)):
            if conductor[i] == conductor_array[j]:
                tiempo_operado[i] = tiempo_operado[i] + tiempo_operado_array[j]

    # Mostrar un total en el reporte
    conductor.append('Total')
    total = 0
    for i in range(len(tiempo_operado)):
        total = total + tiempo_operado[i]
    tiempo_operado.append(total)

    # Uno los valores en una sola lista
    data = zip(conductor, tiempo_operado)

    return data


def reporte_adicionales_por_conductor():
    conductor_array = []
    adicional_conductor_array = []
    adicional_conductor = []
    planilla = Planilla.objects.values('conductor', 'adicional_conductor')

    # Lleno un arreglo con el id de los conductores y los adicionalez
    for value in planilla:
        conductor_array.append(value.get('conductor'))
        adicional_conductor_array.append(value.get('adicional_conductor'))

    # Elimino valores duplicados
    conductor = list(set(conductor_array))

    # Inicializo el arreglo con cero
    for i in range(len(conductor)):
        adicional_conductor.append(0)

    # Realizo sumatoria
    for i in range(len(conductor)):
        for j in range(len(conductor_array)):
            if conductor[i] == conductor_array[j]:
                adicional_conductor[i] = adicional_conductor[i] + adicional_conductor_array[j]

    # Mostrar un total en el reporte
    conductor.append('Total')
    total = 0
    for i in range(len(adicional_conductor)):
        total = total + adicional_conductor[i]
    adicional_conductor.append(total)

    # Uno los valores en una sola lista
    data = zip(conductor, adicional_conductor)

    return data


def reporte_flota_utilizada():
    flota_array = []
    porcentaje_flota = []
    planilla = Planilla.objects.values('flota')

    # Lleno un arreglo con la flota utilizada
    for value in planilla:
        flota_array.append(value.get('flota'))

    # Elimino valores duplicados
    flota = list(set(flota_array))

    # Inicializo el arreglo con cero
    for i in range(len(flota)):
        porcentaje_flota.append(0)

    # Realizo sumatoria
    for i in range(len(flota)):
        for j in range(len(flota_array)):
            if flota[i] == flota_array[j]:
                porcentaje_flota[i] = porcentaje_flota[i] + 1

    # Uno los valores en una sola lista
    data = zip(flota, porcentaje_flota)

    return data
