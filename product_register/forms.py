from django import forms 
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name','brand_name','regular_price_value','offer_price_value','currency','classification_l1','classification_l2','classification_l3','classification_l4','image_url')
        labels = {
            'name':'Full Name',
            'classification_l1': 'CS 1',
            'classification_l2': 'CS 2',
            'classification_l3': 'CS 3',
            'classification_l4': 'CS 4',
        }
    
    def __init__(self,*args, **kwargs):
        super(ProductForm,self).__init__(*args, **kwargs)
        self.fields['name'].required= False
        self.fields['brand_name'].required= False
        self.fields['regular_price_value'].required= False
        self.fields['offer_price_value'].required= False
        self.fields['currency'].required= False
        self.fields['classification_l1'].required= False
        self.fields['classification_l2'].required= False
        self.fields['classification_l3'].required= False
        self.fields['classification_l4'].required= False
        self.fields['image_url'].required= False