from django.shortcuts import redirect
from django.conf import settings
from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin
           
class RequireLoginMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.path in settings.NONE_AUTH_ACCOUNT_PATHS and not request.user.is_authenticated and not request.path.startswith('/admin/'):
            return redirect(settings.LOGIN_URL)
        

class RoleCheckMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path.startswith('/admin/'):
            return
        if hasattr(view_func.view_class, 'rol'):
            rol = getattr(view_func.view_class, 'rol')
            if request.user.usuario.rol != rol:
                return HttpResponseForbidden("Acceso denegado")
        return
           
