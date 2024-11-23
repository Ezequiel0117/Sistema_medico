# aplication/attention/views/citaspordia.py

from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.views import View
from aplication.attention.models import CitaMedica

class CitasPorDiaView(View):
    def get(self, request, *args, **kwargs):
        # Consulta que agrupa las citas médicas por fecha truncada y cuenta la cantidad
        citas_por_dia = CitaMedica.objects.annotate(fecha_truncada=TruncDate('fecha')) \
                                          .values('fecha_truncada') \
                                          .annotate(cantidad=Count('id')) \
                                          .order_by('fecha_truncada')
        
        # Preparamos los datos para pasarlos al contexto
        fechas = [str(cita['fecha_truncada']) for cita in citas_por_dia]
        cantidades = [cita['cantidad'] for cita in citas_por_dia]
        
        # Pasamos las fechas y cantidades al contexto de la plantilla
        context = {
            'citas_por_dia': citas_por_dia,
            'fechas': fechas,
            'cantidades': cantidades
        }
        
        return render(request, 'attention/citas_por_dia.html', context)
