from django.urls import path
from aplication.core.views.home import HomeTemplateView, SigninView, SignoutView, SignupView
from aplication.core.views.btype import BtypeListView, BtypeCreateView, BtypeUpdateView, BtypeDeleteView, BtypeDetailView
from aplication.core.views.patient import PatientCreateView, PatientDeleteView, PatientDetailView, PatientListView, PatientUpdateView
from aplication.core.views.speciality import SpecialityListView, SpecialityCreateView, SpecialityDeleteView, SpecialityDetailView, SpecialityUpdateView
from aplication.core.views.doctor import DoctorCreateView, DoctorDeleteView, DoctorListView, DoctorUpdateView, DoctorDetailView
from aplication.core.views.cargo import CargoListView, CargoDetailView, CargoCreateView, CargoDeleteView, CargoUpdateView
from aplication.core.views.tipomedicamento import TipoMedicamentoListView, TipomedicamentoCreateView, TipoMedicamentoDeleteView, TipoMedicamentotUpdateView, TipoMedicamentoDetailView
from aplication.core.views.marcamedicamento import MarcaMedicamentoListView, MarcaMedicamentoCreateView, MarcaMedicamentoDeleteView, MarcaMedicamentoUpdateView, MarcaMedicamentoDetailView
from aplication.core.views.medicamento import MedicamentoListView, MedicamentoCreateView, MedicamentoDeleteView, MedicamentoUpdateView, MedicamentoDetailView
from aplication.core.views.diagnostico import DiagnosticoListView, DiagnosticoCreateView, DiagnosticoDeleteView, DiagnosticoUpdateView, DiagnosticoDetailView
from aplication.core.views.empleado import EmpleadoListView, EmpleadoCreateView, EmpleadotUpdateView, EmpleadoDeleteView, EmpleadoDetailView
from aplication.core.views.auditoria import AuditoriaListView, AuditoriaDetailView
from aplication.attention.views.Certificado import (
    CertificadoListView, CertificadoCreateView, CertificadoUpdateView, CertificadoDeleteView,CertificadoPDFView
)
from aplication.attention.views.ExamenSolicitado import ExamenSolicitadoCreateView,ExamenSolicitadoDeleteView,ExamenSolicitadoDetailView,ExamenSolicitadoListView,ExamenSolicitadoUpdateView
from aplication.attention.views.CostoAtencion import CostosAtencionCreateView,CostosAtencionListView,CostosAtencionUpdateView,CostosAtencionDeleteView

from aplication.attention.views.CostoAtencionDetalle import (
    CostoAtencionDetalleListView,
    CostoAtencionDetalleCreateView,
    CostoAtencionDetalleUpdateView,
)

app_name='core' # define un espacio de nombre para la aplicacion
urlpatterns = [
  # ruta principal
  path('', HomeTemplateView.as_view(),name='home'),
  path('signup/', SignupView.as_view(), name='signup'),
  path('logout/', SignoutView.as_view(), name='logout'),
  path('signin/', SigninView.as_view(), name='signin'),
  # rutas doctores VBC
  path('patient_list/',PatientListView.as_view() ,name="patient_list"),
  path('patient_create/', PatientCreateView.as_view(),name="patient_create"),
  path('patient_update/<int:pk>/', PatientUpdateView.as_view(),name='patient_update'),
  path('patient_delete/<int:pk>/', PatientDeleteView.as_view(),name='patient_delete'),
  path('patient_detail/<int:pk>/', PatientDetailView.as_view(),name='patient_detail'),
  #Tipo de sangre:
  path('type_list/',BtypeListView.as_view() ,name="type_list"),
  path('type_create/', BtypeCreateView.as_view(),name="type_create"),
  path('type_update/<int:pk>/', BtypeUpdateView.as_view(),name='type_update'),
  path('type_delete/<int:pk>/', BtypeDeleteView.as_view(),name='type_delete'),
  path('type_detail/<int:pk>/', BtypeDetailView.as_view(),name='type_detail'),
  #Especialidades
  path('speciality_list/', SpecialityListView.as_view() ,name="speciality_list"),
  path('speciality_create/', SpecialityCreateView.as_view(), name="speciality_create"),
  path('speciality_update/<int:pk>/', SpecialityUpdateView.as_view(), name='speciality_update'),
  path('speciality_delete/<int:pk>/', SpecialityDeleteView.as_view(), name='speciality_delete'),
  path('speciality_detail/<int:pk>/', SpecialityDetailView.as_view(), name='speciality_detail'),
  #Doctor
  path('doctor_list/', DoctorListView.as_view(), name="doctor_list"),
  path('doctor_create/', DoctorCreateView.as_view(), name="doctor_create"),
  path('doctor_update/<int:pk>/', DoctorUpdateView.as_view(), name='doctor_update'),
  path('doctor_delete/<int:pk>/', DoctorDeleteView.as_view(), name='doctor_delete'),
  path('doctor_detail/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
  #Cargos
  path('cargo_list/', CargoListView.as_view(), name="cargo_list"),
  path('cargo_create/', CargoCreateView.as_view(), name="cargo_create"),
  path('cargo_update/<int:pk>/', CargoUpdateView.as_view(), name='cargo_update'),
  path('cargo_delete/<int:pk>/', CargoDeleteView.as_view(), name='cargo_delete'),
  path('cargo_detail/<int:pk>/', CargoDetailView.as_view(), name='cargo_detail'),
  #Tipo medicamentos
  path('tipom_list/', TipoMedicamentoListView.as_view(), name="tipom_list"),
  path('tipom_create/', TipomedicamentoCreateView.as_view(), name="tipom_create"),
  path('tipom_update/<int:pk>/', TipoMedicamentotUpdateView.as_view(), name="tipom_update"),
  path('tipom_delete/<int:pk>/', TipoMedicamentoDeleteView.as_view(), name="tipom_delete"),
  path('tipom_detail/<int:pk>/', TipoMedicamentoDetailView.as_view(), name='tipom_detail'),
  #Marca Medicamento
  path('marca_list/', MarcaMedicamentoListView.as_view(), name="marca_list"),
  path('marca_create/', MarcaMedicamentoCreateView.as_view(), name="marca_create"),
  path('marca_update/<int:pk>/',MarcaMedicamentoUpdateView.as_view(), name='marca_update'),
  path('marca_delete/<int:pk>/', MarcaMedicamentoDeleteView.as_view(), name='marca_delete'),
  path('marca_detail/<int:pk>/', MarcaMedicamentoDetailView.as_view(), name='marca_detail'),
  #Medicamentos
  path('medicamento_list/', MedicamentoListView.as_view(), name="medicamento_list"),
  path('medicamento_create/', MedicamentoCreateView.as_view(), name="medicamento_create"),
  path('medicamento_update/<int:pk>/',MedicamentoUpdateView.as_view(), name='medicamento_update'),
  path('medicamento_delete/<int:pk>/',MedicamentoDeleteView.as_view(), name='medicamento_delete'),
  path('medicamento_detail/<int:pk>/', MedicamentoDetailView.as_view(), name='medicamento_detail'),
  #Diagnosticos
  path('diagnostico_list/', DiagnosticoListView.as_view(), name="diagnostico_list"),
  path('diagnostico_create/', DiagnosticoCreateView.as_view(), name="diagnostico_create"),
  path('diagnostico_update/<int:pk>/',DiagnosticoUpdateView.as_view(), name='diagnostico_update'),
  path('diagnostico_delete/<int:pk>/', DiagnosticoDeleteView.as_view(), name='diagnostico_delete'),
  path('diagnostico_detail/<int:pk>/', DiagnosticoDetailView.as_view(), name='diagnostico_detail'),
  #Empleados
  path('empleado_list/', EmpleadoListView.as_view(), name="empleado_list"),
  path('empleado_create/', EmpleadoCreateView.as_view(), name="empleado_create"),
  path('empleado_update/<int:pk>/',EmpleadotUpdateView.as_view(), name='empleado_update'),
  path('empleado_delete/<int:pk>/', EmpleadoDeleteView.as_view(), name='empleado_delete'),
  path('empleado_detail/<int:pk>/', EmpleadoDetailView.as_view(), name='empleado_detail'),
  #Auditorias
  path('auditoria_list/', AuditoriaListView.as_view(), name="auditoria_list"),
  path('auditoria_detail/<int:pk>/', AuditoriaDetailView.as_view(), name='auditoria_detail'),
  #Certificados
  path('certificaDO', CertificadoListView.as_view(), name='listacertificado'),
  path('nuevo11/', CertificadoCreateView.as_view(), name='crearcertificado'),
  path('editar/<int:pk>/', CertificadoUpdateView.as_view(), name='editarcertificado'),
  path('eliminar/<int:pk>/', CertificadoDeleteView.as_view(), name='eliminarcertificado'),
  path('certificado/<int:pk>/pdf/', CertificadoPDFView.as_view(), name='certificado_pdf'),
  #Ruta de Examen solicitado
  path('ExamenSolicitado/', ExamenSolicitadoListView.as_view(), name='ExamenSolicitado_list'),
  path('ExamenSolicitado5/<int:pk>/', ExamenSolicitadoDetailView.as_view(), name='ExamenSolicitado_detail'),
  path('ExamenSolicitado3/nuevo/', ExamenSolicitadoCreateView.as_view(), name='ExamenSolicitado_create'),
  path('ExamenSolicitado1/<int:pk>/editar/', ExamenSolicitadoUpdateView.as_view(), name='ExamenSolicitado_edit'),
  path('ExamenSolicitado2/<int:pk>/eliminar/', ExamenSolicitadoDeleteView.as_view(), name='ExamenSolicitado_delete'),
  #Detalle Atencion
  path('detalleatencion1', CostoAtencionDetalleListView.as_view(), name='costos_atencion_detalle_list'),
  path('nuevo/', CostoAtencionDetalleCreateView.as_view(), name='costos_atencion_detalle_create'),
  path('<int:pk>/editar/', CostoAtencionDetalleUpdateView.as_view(), name='costos_atencion_detalle_update'),
  #Costos de Atencion
  path('costos-atencion/', CostosAtencionListView.as_view(), name='CostosAtencion_list'),
  path('costos-atencion1/nuevo/', CostosAtencionCreateView.as_view(), name='CostosAtencion_create'),
  path('costos-atencion2/<int:pk>/editar/', CostosAtencionUpdateView.as_view(), name='CostosAtencion_edit'),
  path('costos-atencion3/<int:pk>/eliminar/', CostosAtencionDeleteView.as_view(), name='CostosAtencion_eliminar'),
]