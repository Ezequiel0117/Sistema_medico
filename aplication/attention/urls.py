from django.urls import path
from aplication.attention.views.medical_attention import AttentionCreateView, AttentionDetailView, AttentionListView, AttentionUpdateView
from aplication.core.views.home import HomeTemplateView
from aplication.core.views.patient import PatientCreateView, PatientDeleteView, PatientDetailView, PatientListView, PatientUpdateView
from aplication.attention.views.horarioatencion import *
from aplication.attention.views.citamedicam import *
from aplication.attention.views.serviciosadd import *
from aplication.attention.views.costosadicionales import CostosAtencionListView, CostosAtencionCreateView, CostosAtencionUpdateView
from aplication.attention.views.fichamedica import generar_ficha_medica_pdf, FichaMedicaView
from aplication.attention.views.citaspordia import CitasPorDiaView
from aplication.attention.views.PaypalPayment import (
    PagoListView,
    PagoCreateView,
    PagoDetailView,
    PagoDeleteView,
    PagoComprobanteView,
    paypal_execute,
    verificar_pago_paciente,
)

 
app_name='attention' # define un espacio de nombre para la aplicacion
urlpatterns = [
  # rutas de atenciones
  path('attention_list/',AttentionListView.as_view() ,name="attention_list"),
  path('attention_create/', AttentionCreateView.as_view(),name="attention_create"),
  path('attention_update/<int:pk>/', AttentionUpdateView.as_view(),name='attention_update'),
  path('attention_detail/<int:pk>/', AttentionDetailView.as_view(),name='attention_detail'),
  # path('patient_delete/<int:pk>/', PatientDeleteView.as_view(),name='patient_delete'),
  
  #Horario atencion
  path('horarioatencion_list/', HorarioAtencionListView.as_view(), name="horarioatencion_list"),
  path('horarioatencion_create/', HorarioAtencionCreateView.as_view(), name="horarioatencion_create"),
  path('horarioatencion_update/<int:pk>/',HorarioAtencionUpdateView.as_view(), name='horarioatencion_update'),
  path('horarioatencion_delete/<int:pk>/', HorarioAtencionDeleteView.as_view(), name='horarioatencion_delete'),
  path('horarioatencion_detail/<int:pk>/', HorarioAtencionDetailView.as_view(), name='horarioatencion_detail'),
  #Cita medicas
  path('citamedica_list/', CitaMedicaListView.as_view(), name="citamedica_list"),
  path('citamedica_create/', CitaMedicaCreateView.as_view(), name="citamedica_create"),
  path('citamedica_update/<int:pk>/',CitaMedicaUpdateView.as_view(), name='citamedica_update'),
  path('citamedica_delete/<int:pk>/', CitaMedicaDeleteView.as_view(), name='citamedica_delete'),
  path('citamedica_detail/<int:pk>/', CitaMedicaFDetailView.as_view(), name='citamedica_detail'),
  #Servicios Extras
  path('servicio_list/', ServiciosAdicionalesListView.as_view(), name="servicio_list"),
  path('servicio_create/', ServiciosAdicionalesCreateView.as_view(), name="servicio_create"),
  path('servicio_update/<int:pk>/',ServiciosAdicionalesUpdateView.as_view(), name='servicio_update'),
  path('servicio_delete/<int:pk>/', ServiciosAdicionalesDeleteView.as_view(), name='servicio_delete'),
  path('servicio_detail/<int:pk>/', ServiciosAdicionalesDetailView.as_view(), name='servicio_detail'),
  #FichaMedica
  path('ficha_medica/<int:paciente_id>/', FichaMedicaView.as_view(), name='ficha_medica'),
  path('ficha_medica/pdf/<int:paciente_id>/', generar_ficha_medica_pdf, name='generar_ficha_medica_pdf'),
  #CostosAtenciones
  path('costos_list/', CostosAtencionListView.as_view(), name="costos_list"),
  path('costos_create/', CostosAtencionCreateView.as_view(), name="costos_create"),
  path('costos_update/<int:pk>/', CostosAtencionUpdateView.as_view(),name='costos_update'),
  #Grafico
  path('citas_por_dia/', CitasPorDiaView.as_view(), name='citas_por_dia'),
  
  # path('patient_delete/<int:pk>/', PatientDeleteView.as_view(),name='patient_delete'),
  path('pagos/', PagoListView.as_view(), name='pago_list'),
  path('pagos/crear/', PagoCreateView.as_view(), name='pago_create'),
  path('pagos/detalle/<int:pk>/', PagoDetailView.as_view(), name='pago_detail'),
  path('pagos/eliminar/<int:pk>/', PagoDeleteView.as_view(), name='pago_delete'),
  path('pagos/comprobante/<int:pk>/', PagoComprobanteView.as_view(), name='pago_comprobante'),
  path('paypal/execute/', paypal_execute, name='paypal_execute'),
  path('verificar_pago_paciente/', verificar_pago_paciente, name='verificar_pago_paciente'),
  
  
  
]
