from django import forms
from .models import Provider, Product, Entry, Sale, Inventory

#create your forms

class ProviderForm(forms.ModelForm):
	class Meta:
		model = Provider
		fields = [
				'name',
				'adrress',
				'phone',
				'email',
		]

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = [
				'name',
				'price',
				'presentation',
				'user',
				'providers',
		]

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = [
				'product',
				'cant',
		]

class SaleForm(forms.ModelForm):
	class Meta:
		model = Sale
		fields = [
				'user_name',
				'product',
				'cant',
				'totalPrice',
		]

class InventoryForm(forms.ModelForm):
	class Meta:
		model = Inventory
		fields = [
				'product',
				'cant',
				'name_product',
				'price_product',
		]