from django.utils.deprecation import MiddlewareMixin
from django.utils import timezone

from utils import createError
from authenticator.models import Auth
from person.models import Person

class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):

        if request.path == '/':
            return None

        if request.path.startswith('/form/login/'):
            return None

        if request.path.startswith('/form/signup/'):
            return None

        if request.path.startswith('/auth/login/'):
            return None

        if request.path.startswith('/auth/signup/'):
            return None

        if request.path.startswith('/all/'):
            return None

        if request.path.startswith('/admin/'):
            return None 

        if 'AUTHENTICATION' not in request.COOKIES:
            return createError('Login first.')

        token = request.COOKIES.get('AUTHENTICATION')
        auth = None
        try:
            auth = Auth.objects.get(code=token)
        except:
            return createError('No authentication token.')

        if timezone.now() > auth.expiredTime:
            return createError('Session expired.')

        try:
            currentPerson = Person.objects.get(id=auth.user_id)
        except:
            createError('Person not found.')
        request.META['CURRENT_PERSON'] = currentPerson

        return None
