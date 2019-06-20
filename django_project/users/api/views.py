from rest_framework.generics import CreateAPIView
from .serializers import UserCreateSerializer,LoginSerializer
from django.contrib.auth.admin import User
from rest_framework.views import APIView
from django.contrib.auth import login,logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

 
class UserCreateAPIView(CreateAPIView):
	queryset=User.objects.all()	
	serializer_class=UserCreateSerializer


class LoginAPIView(APIView):
	
	def post(self,request):
		serializer=LoginSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user=serializer.validated_data['user']
		login(request,user)
		token,created=Token.objects.get_or_create(user=user)
		return Response({'token':token.key},status=200)

class LogoutAPIView(APIView):
	authentication_classes=(TokenAuthentication,)
	
	def post(self,request):
		logout(request)
		return Response(status=204)	
	
    
	

