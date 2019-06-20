from django import forms
from . import models

class DocumentForm(forms.ModelForm):
	class Meta:
		model = models.Filedata
		fields = ('filename', 'userfile')
