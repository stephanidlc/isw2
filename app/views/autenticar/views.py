from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from app.forms import LoginForm
from django.shortcuts import redirect

class Login(LoginView):
  # redirect_authenticated_user = 1
  template_name = 'autenticacion/login.html'
  authentication_form = LoginForm
  success_url = 'login'
  
  def post(self, request, *args, **kwargs):
    usuario = request.POST['username']
    contrasenna = request.POST['password']
    user = authenticate(username = usuario, password = contrasenna)
    if user is not None:
      login(self.request, user)
      match( user.usuario.rol):
        case 'estudiante':
          return redirect('listar_solicitudes')
        case 'secretario':
          return redirect('listar_estudiantes')
        case 'decano':
          pass
    return super().post(request, *args, **kwargs)


class CustomLogoutView(LogoutView):
    next_page = 'login'
