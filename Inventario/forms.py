from django import forms
from .models import Provider, Product, Entry, Sale

#create your forms

class ProviderForm():
	class Meta:
		model = Provider
		fields = [
				'name',
				'adrress',
				'phone',
				'email',
		]

class ProductForm():
	class Meta:
		model = Product
		fields = [
				'name',
				'price',
				'presentation',
				'user',
				'providers',
				'created_at',
		]

class EntryForm():
	class Meta:
		model = Entry
		fields = [
				'product',
				'cant',
				'created_at',
		]

class SaleForm():
	class Meta:
		model = Sale
		fields = [
				'user_name',
				'product',
				'cant',
				'created_at'
		]

class Inventory():
	class Meta:
		model = Inventory
		fields = [
				'product',
				'cant',
				'name_product',
				'price_product',
				'entry_date',
		]