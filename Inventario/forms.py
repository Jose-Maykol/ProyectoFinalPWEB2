from django import forms
from .models import Provider, Product, Entry, Sale, Inventory, Client, Store

#create your forms
class StoreForm(forms.ModelForm):
	class Meta:
		model = Store
		fields = [
				'store_name',
				'location',
		]

class ClientForm(forms.ModelForm):
	class Meta:
		model = Client
		fields = [
				'customer_name',
				'phone',
				'email',
				'razon_social',
				'RUC',
		]

class ProviderForm(forms.ModelForm):
	class Meta:
		model = Provider
		fields = [
				'name',
				'adrress',
				'phone',
				'email',
				'RUC',
				'razon_social',
		]

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = [
				'name',
				'img',
				'price',
				'presentation',
				'user',
				'providers',
				'line',
		]

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = [
				'store',
				'product',
				'cant',
		]

class SaleForm(forms.ModelForm):
	class Meta:
		model = Sale
		fields = [
				'user_name',
				'client',
				'product',
				'store',
				'cant',
				'total_price',
		]

class InventoryForm(forms.ModelForm):
	class Meta:
		model = Inventory
		fields = [
				'store',
				'product',
				'cant',
				'name_product',
				'presentation',
				'price_product',
				'providers',
				'line',
		]