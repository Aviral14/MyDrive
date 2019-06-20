from rest_framework.generics import ListAPIView,UpdateAPIView,CreateAPIView,DestroyAPIView
from Dashboard.models import Filedata
from .serializers import FiledataListSerializer,FiledataUpdateSerializer,FiledataCreateSerializer,FiledataDeleteSerializer
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
import firebase_utilities.helper_functions as firebase
import re

class FiledataListAPIView(ListAPIView):
	serializer_class=FiledataListSerializer
	permission_classes=[IsAuthenticated]

	def get_queryset(self):
		user_obj=self.request.user
		q_set=user_obj.filedata_set.all()
		if not q_set:
			list=firebase.list_files(user_obj.username) 
			return list
		else:
			return q_set
		
class FiledataUpdateAPIView(UpdateAPIView):
	queryset=Filedata.objects.all()	
	serializer_class=FiledataUpdateSerializer
	permission_classes=[IsAuthenticated]
	lookup_field='filename'

	def is_unique(self):
		file_objs=Filedata.objects.filter(user=self.request.user)
		if file_objs:		
			for obj in file_objs:
				if obj.filename==self.request.data.get('filename',''):
					msg='This File Name Already Exists! Try Again with a different name'
					raise exceptions.ValidationError(msg) 
		else:
			file_objs=fire_base.list_files(self.request.user.username)
			for obj in file_objs:
				if obj.filename==self.request.data.get('filename',''):
					msg='This File Name Already Exists! Try Again with a different name'
					raise exceptions.ValidationError(msg)
			
		
	def get_original_name(self):
		regex_obj=re.compile(r'\w+')
		return regex_obj.findall(self.request.get_full_path())[-1]
	
	def perform_update(self, serializer):
		self.is_unique()
		original_name=self.get_original_name()
		blob_name=self.request.user.username+'/'+original_name
		destinantion_blob_name=self.request.user.username+'/'+self.request.data['filename']
		firebase.update_files(blob_name,destinantion_blob_name)
		return serializer.save(user=self.request.user)
    
	
class FiledataCreateAPIView(CreateAPIView):
	queryset=Filedata.objects.all()	
	serializer_class=FiledataCreateSerializer
	permission_classes = [IsAuthenticated]

	def is_unique(self):
		file_objs=Filedata.objects.filter(user=self.request.user)
		if file_objs:		
			for obj in file_objs:
				if obj.filename==self.request.data.get('filename',''):
					msg='This File Name Already Exists! Try Again with a different name'
					raise exceptions.ValidationError(msg) 
		
	def perform_create(self,serializer):
		self.is_unique()
		serializer.save(user=self.request.user)
		user_obj=self.request.user
		file_path=str(user_obj.filedata_set.filter(filename=self.request.data['filename'])[0].userfile)
		absolute_file_path='BASE_DIR/media/'+file_path
		destination_blob_name=self.request.user.username+'/'+self.request.data['filename']
		firebase.upload_files(absolute_file_path,destination_blob_name)

class FiledataDeleteAPIView(DestroyAPIView):
	queryset=Filedata.objects.all()	
	serializer_class=FiledataDeleteSerializer
	permission_classes = [IsAuthenticated]
	lookup_field='filename'

	def get_original_name(self):
		regex_obj=re.compile(r'\w+')
		return regex_obj.findall(self.request.get_full_path())[-1]

	def perform_destroy(self,instance):
		original_name=self.get_original_name()
		blob_name=self.request.user.username+'/'+original_name	
		firebase.delete_files(blob_name)
		Filedata.objects.filter(filename=original_name).delete()
		
	


	

    

    

