from django import forms
from .models import ProductComments,Product


class comment_form(forms.ModelForm):
    product = forms.CharField(widget = forms.HiddenInput(), required = False)
    user    = forms.CharField(widget = forms.HiddenInput(), required = False)
    class Meta():
        model= ProductComments
        fields = ['user','product','comment','rating']

class ProductForm(forms.ModelForm):
    class Meta():
        model= Product
        fields = [
                    'category',      
                    'title',                  
                    'description',   
                    'price',         
                    'image',         
                    'featured',      
                    'active',        
                    'is_digital',    
                ]

