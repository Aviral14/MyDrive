from rest_framework.serializers import ModelSerializer
from django.contrib.auth.admin import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework import exceptions

class UserCreateSerializer(ModelSerializer):
	class Meta:
		model=User
		fields=['username','password']
		extra_kwargs={'password':{'write_only':True}}

	def create(self,validated_data):
		username=validated_data['username']
		password=validated_data['password']
		user_obj=User(username=username)
		user_obj.set_password(password)
		user_obj.save()
		return validated_data

class LoginSerializer(serializers.Serializer):
	username=serializers.CharField() 
	password=serializers.CharField()     

	def validate(self,data):
		username=data.get('username','') 
		password=data.get('password','') 
	
		if username and password:
			user=authenticate(username=username,password=password)
			if user:
				if user.is_active:
					data['user']=user
				else:
					msg='User is Deactivated'
					raise exceptions.ValidationError(msg)
			else:
				msg='Wrong Login Credentials'
				raise exceptions.ValidationError(msg)
		else:
			msg='Provide both username and Password'
			raise exceptions.ValidationError(msg)
		return data
			
