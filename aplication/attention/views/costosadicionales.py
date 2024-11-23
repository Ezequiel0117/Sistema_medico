from django.utils import timezone
from decimal import Decimal
import json
from django.urls import reverse_lazy
from django.db import transaction
from django.shortcuts import render
# from aplication.attention.forms.costos_atencion import 
from aplication.attention.models import CostosAtencion, CostoAtencionDetalle, ServiciosAdicionales, Atencion
from aplication.attention.forms.costos_atencion import CostoAtencionForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from aplication.core.models import Diagnostico, Medicamento
from doctor.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, UpdateViewMixin
from doctor.utils import custom_serializer, save_audit

# class CostosAtencionListView(LoginRequiredMixin,ListViewMixin,ListView):
#     template_name = "attention/costos_atencion/list.html"
#     model = CostosAtencion
#     context_object_name = 'costos'
#     # query = None
#     # paginate_by = 2
    
#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#         # context['title'] = "SaludSync"
#         # context['title1'] = "Consulta de Pacientes"
#         # return context
        
        
# Vista para listar costos asociados a una atención
class CostosAtencionListView(LoginRequiredMixin, ListView):
    model = CostosAtencion
    template_name = "attention/costos_atencion/list.html"
    context_object_name = "costos"
    paginate_by = 10  # Opcional, para paginar resultados

    def get_queryset(self):
        return self.model.objects.filter(activo=True).select_related("atencion")




    
class CostosAtencionCreateView(LoginRequiredMixin, CreateView):
    model = CostosAtencion
    template_name = 'attention/costos_atencion/form.html'
    form_class = CostoAtencionForm  # Asegúrate de tener este formulario
    success_url = reverse_lazy('attention:costos_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicios_adicionales'] = ServiciosAdicionales.objects.all()  # Trae los servicios disponibles
        return context
    
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        servicios = data['servicios']
        
        try:
            with transaction.atomic():
                # Crear la instancia del modelo CostosAtencion
                print("Creando CostosAtencion")
                costosAtencion = CostosAtencion.objects.create(
                    atencion_id=int(data['atencion']),
                    total=Decimal(data['total']),
                    activo=data.get('activo', True)  # Si se incluye en los datos
                )

                # Registrar los servicios adicionales
                print("Procesando servicios adicionales")
                for servicio in servicios:
                    CostoAtencionDetalle.objects.create(
                        costo_atencion=costosAtencion,  # Relación con CostosAtencion
                        servicios_adicionales_id=int(servicio['codigo']),  # Asegúrate de que el campo sea correcto
                        costo_servicio=Decimal(servicio['costo_servicio']),
                    )

                # Registrar auditoría
                atencion = Atencion.objects.get(id=data['atencion'])  # Obtener la atención asociada
                save_audit(request, atencion, "A")  # Guardar auditoría con la atención correcta

                messages.success(self.request, f"Éxito al registrar la atención médica #{atencion.id}")
                return JsonResponse({"msg": "Éxito al registrar la atención médica."}, status=200)

        except Exception as ex:
            messages.error(self.request, f"Error al registrar la atención médica: {str(ex)}")
            return JsonResponse({"msg": str(ex)}, status=400)

        
class CostosAtencionUpdateView(LoginRequiredMixin, UpdateView):
    model = CostosAtencion
    template_name = 'attention/costos_atencion/form.html'
    form_class = CostoAtencionForm  # Asegúrate de tener este formulario
    success_url = reverse_lazy('attention:costos_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Trae los servicios disponibles y los ordena por nombre_servicio
        context['servicios_adicionales'] = ServiciosAdicionales.objects.values('id', 'nombre_servicio').order_by('nombre_servicio')
        
        # Obtenemos los detalles actuales de costos para mostrarlos en el formulario
        costos_atencion = self.get_object()  # Obtén el objeto de CostosAtencion actual
        detail_costos = list(CostoAtencionDetalle.objects.filter(costo_atencion_id=costos_atencion.id).values("servicios_adicionales_id", "servicios_adicionales__nombre_servicio", "costo_servicio"))
        
        # Convertimos a JSON y lo agregamos al contexto
        context['detail_costos'] = json.dumps(detail_costos, default=custom_serializer)

        return context

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        servicios = data['servicios']
        
        try:
            # Obtener la instancia de CostosAtencion que se actualizará
            costosAtencion = self.get_object()

            with transaction.atomic():
                # Actualizar el registro de CostosAtencion
                costosAtencion.atencion_id = int(data['atencion'])
                costosAtencion.total = Decimal(data['total'])
                costosAtencion.activo = data.get('activo', True)  # Si se incluye en los datos
                costosAtencion.save()

                # Borrar los detalles de servicios anteriores
                CostoAtencionDetalle.objects.filter(costo_atencion_id=costosAtencion.id).delete()

                # Registrar los nuevos servicios adicionales
                print("Procesando servicios adicionales")
                for servicio in servicios:
                    CostoAtencionDetalle.objects.create(
                        costo_atencion=costosAtencion,  # Relación con CostosAtencion
                        servicios_adicionales_id=int(servicio['codigo']),  # Asegúrate de que el campo sea correcto
                        costo_servicio=Decimal(servicio['costo_servicio']),
                    )

                # Registrar auditoría
                atencion = costosAtencion.atencion  # Obtener la atención asociada
                save_audit(request, atencion, "M")  # Guardar auditoría con la atención correcta

                # Enviar un mensaje de éxito y devolver respuesta JSON
                messages.success(self.request, f"Éxito al actualizar los costos de atención médica #{costosAtencion.id}")
                return JsonResponse({"msg": "Éxito al actualizar los costos de atención médica."}, status=200)

        except Exception as ex:
            # Manejo de excepciones y mensajes de error
            messages.error(self.request, f"Error al actualizar los costos de atención médica: {str(ex)}")
            return JsonResponse({"msg": str(ex)}, status=400)





        
# class AttentionDetailView(LoginRequiredMixin,DetailView):
#     model = Atencion
    
#     def get(self, request, *args, **kwargs):
#         print("entro get")
#         atencion = self.get_object()
#         print(atencion)
#         detail_atencion =list(DetalleAtencion.objects.filter(atencion_id=atencion.id).values("medicamento_id","medicamento__nombre","cantidad","prescripcion"))
#         detail_atencion=json.dumps(detail_atencion,default=custom_serializer)
#         data = {
#             'id': atencion.id,
#             'nombres': atencion.paciente.nombre_completo,
#             'foto': atencion.paciente.get_image(),
#             'detalle_atencion': detail_atencion
#         }
#         print(data)
#         return JsonResponse(data)