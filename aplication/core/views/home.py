# from django.views.generic import TemplateView

# from aplication.core.models import Paciente

# class HomeTemplateView(TemplateView):
#     template_name = 'core/home.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context = {"title": "SaludSync","title1": "Sistema Medico", "title2": "Sistema Medico"}
#         context["can_paci"] = Paciente.cantidad_pacientes()
#         print(context["can_paci"])
#         return context
    


from datetime import date
from aplication.attention.models import Atencion, CitaMedica
from aplication.core.models import Paciente

from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView, View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db import IntegrityError



# Vista para la página principal
class HomeTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["title"] = "SaludSync"
            context["title1"] = "Sistema Médico"
            context["title2"] = "Sistema Médico"
            context["can_paci"] = Paciente.cantidad_pacientes()
            context["can_atencion"] = Atencion.cantidad_atencion()
            context["ultimo_paciente"] = Paciente.objects.order_by('-id').first()
            context["can_cita"] = CitaMedica.cantidad_cita()
            context["proximas_citas"] = CitaMedica.objects.filter(fecha=date.today(), estado='P').order_by('hora_cita')
            context["ultima_cita_completada"] = CitaMedica.objects.filter(estado='R').order_by('-fecha', '-hora_cita').first()
            context["ultima_cita"] = CitaMedica.objects.order_by('-fecha', '-hora_cita').first()
            return context


# Vista para registrar usuarios
class SignupView(FormView):
    template_name = "partials/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('core:home')

    def form_valid(self, form):
        try:
            user = form.save()
            login(self.request, user)  # Inicia sesión automáticamente
            return super().form_valid(form)
        except IntegrityError:
            form.add_error(None, "El nombre de usuario ya existe")
            return self.form_invalid(form)

    def form_invalid(self, form):
        form.add_error(None, "Las contraseñas no coinciden" if 'password2' in form.errors else "Error al registrar el usuario")
        return super().form_invalid(form)


# Vista para cerrar sesión
class SignoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('core:home')


# Vista para iniciar sesión
class SigninView(FormView):
    template_name = "partials/signin.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy('core:home')

    def form_valid(self, form):
        user = authenticate(
            self.request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, "Nombre de usuario o contraseña incorrectos")
            return self.form_invalid(form)
            return redirect('core:home')  # Redirige al home usando el nombre de la URL

    
    