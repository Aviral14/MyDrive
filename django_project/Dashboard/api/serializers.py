from rest_framework.serializers import ModelSerializer
from Dashboard.models import Filedata

class FiledataListSerializer(ModelSerializer):
	class Meta:
		model=Filedata
		fields=['user','userfile','filename','uploaded_at']

class FiledataUpdateSerializer(ModelSerializer):
	class Meta:
		model=Filedata
		fields=['filename',]

class FiledataCreateSerializer(ModelSerializer):
	class Meta:
		model=Filedata
		fields=['userfile','filename']


class FiledataDeleteSerializer(ModelSerializer):
	class Meta:
		model=Filedata
		fields=['user','userfile','filename','uploaded_at']
