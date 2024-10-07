from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import SignUpForm

@api_view(['POST'])
def signup(request):
    data = request.data
    message = 'success'

    form = SignUpForm({
        'email': data.get('email'),
        'name': data.get('name'),
        'password1': data.get('password1'),
        'password2': data.get('password2')
    })

    if form.is_valid():
        form.save()
        # Send verification message ---> Later
    else:
        message = 'error'

    return JsonResponse({'status':message})