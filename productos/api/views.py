import json

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse

from productos.models import Producto
from .serializer import ProductSerializer

@api_view(['GET',])
@permission_classes((AllowAny,))
def hola(request):
    return Response({"message": "holaa"})

@api_view(['GET',])
@permission_classes((AllowAny,))
def product_list(request):
    objects = Producto.objects.all()
    serializer_class = ProductSerializer(objects, many=True)
    return JsonResponse(serializer_class.data,safe=False,status=200)



@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def private_endpoint(request):
    return JsonResponse({"message":"este endpoint solo para user registrados"},status=200)




def is_venta(user):
    return user.groups.filter(name='ventas').exists()

@api_view(['GET',])
@permission_classes((IsAuthenticated,))
@user_passes_test(is_venta)
def endpoint_venta(request):
    return JsonResponse({"message":"solo para el grupo de venta"})




@api_view(['POST',])
@permission_classes((AllowAny,))
def login_user(request):
    if ( request.body ):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        if username is None:
            return JsonResponse({"errors": {"detail": "Please enter username"}}, status=400)
        elif password is None:
            return JsonResponse({"errors": {"detail": "Please enter password"}}, status=400)

        # authentication user
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"success": "User has been logged in"})
        return JsonResponse({"errors": "Invalid credentials"},status=400,)
    else:
        return JsonResponse({"error":"no data on body"},status=500)
    
@api_view(['POST'])
@permission_classes((AllowAny,))
def logout_user(request):
    logout(request)
    return JsonResponse({"exit": "logout success"},status=201)