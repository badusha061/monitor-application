from .serializers import UserSerializer , CustomerTokenObtainPairSerialzer 
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .task import add
from rest_framework.response import Response

class UserRegistration(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()




class CustomerTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomerTokenObtainPairSerialzer


class TestCelery(APIView):
    def get(self,request):
        print('hello world')
        result  = add.delay(10,10)
        print(result)
        return Response(data=result)