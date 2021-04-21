from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets

from rest_framework.authtoken.models import Token
from manageAPI.api.serializers import userRegisterS, BusinessSerializers, productSerializers
from manageAPI.models import User, Business, Products


@api_view(['GET'])
def indexView(request):
    """
    its a function which give info about api urls
    """
    data = {
        'Create User': 'http://127.0.0.1:8000/manageAPI/register with username, email, password, password2',
        'login': 'http://127.0.0.1:8000/manageAPI/login',
        'BusinessBusinessView': 'http://127.0.0.1:8000/manageAPI/manage/BusinessView/',
        'product View': 'http://127.0.0.1:8000/manageAPI/manage/ProductView/',
        'product update': 'http://127.0.0.1:8000/manageAPI/manage/ProductView/<int:pk>'
    }
    return Response(data)


class userRegisterView(APIView):
    """for creating user"""

    def post(self, request):
        serilizer = userRegisterS(data=request.data)
        data = {}
        if serilizer.is_valid():
            acc = serilizer.save()
            data['respose'] = "success register a new user."
            data['email'] = serilizer.validated_data.get('email')
            data['username'] = serilizer.validated_data.get('username')
            token = Token.objects.get(user=acc).key
            print(token)
            data['token'] = token
        else:
            return Response(
                serilizer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(data)


class BusinessView(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializers

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


class ProductView(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = productSerializers

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)

    def destroy(self, request, pk=None, *args, **kwargs):
        pr = self.get_object()
        self.perform_destroy(instance=pr)
        return Response({'Http_method': 'Delete'})

    def update(self, request,pk=None, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)
