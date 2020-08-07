from django import forms
from .models import Provider

#create your forms

class ProviderForm():
	class Meta:
		model = Provider
		fields = [
				'name',
				'adrress',
				'phone',
				'email'
		]