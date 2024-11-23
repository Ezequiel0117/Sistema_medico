from django.shortcuts import get_object_or_404, render
from django.views import View
from aplication.core.models import Paciente
from aplication.attention.models import Atencion
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from django.utils import timezone

class FichaMedicaView(View):
    template_name = 'attention/fichamedica/ficha_medica.html'

    def get(self, request, paciente_id):
        paciente = get_object_or_404(Paciente, id=paciente_id)
        atenciones = Atencion.objects.filter(paciente=paciente).order_by('-fecha_atencion')
        
        context = {
            'paciente': paciente,
            'atenciones': atenciones,
        }
        return render(request, self.template_name, context)


def generar_ficha_medica_pdf(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    atenciones = Atencion.objects.filter(paciente=paciente).order_by('-fecha_atencion')

    # Renderizar plantilla HTML a cadena
    html_string = render_to_string('attention/fichamedica/ficha_medica_pdf.html', {
        'paciente': paciente,
        'atenciones': atenciones,
        'fecha_actual': timezone.now()
    })

    # Generar el PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="Ficha_Medica_{paciente.cedula}.pdf"'

    html = HTML(string=html_string)
    pdf = html.write_pdf()
    response.write(pdf)

    return response

# Create your views here.
