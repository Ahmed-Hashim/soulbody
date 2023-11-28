from .models import*
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['en_name','en_description','ar_name','ar_description','price']
        name=forms.CharField(label="Service Name")
        description=forms.CharField(label="Description")
        price=forms.CharField(label="Price")
        widgets={
            'created_by':forms.TextInput(attrs={'id':'created-by',"type":"hidden",})
        }
class InvoiceForm(forms.ModelForm):
    class Meta:
        model=Invoice
        fields=[
            'customerid',
            'employeeid',
            'note',
            'status',
            'products',
            'paymentTerms',
            'discount_presentage'
        ]
        customerid=forms.CharField()
        employeeid=forms.CharField()
        note=forms.CharField()
        status=forms.CharField()
        products=forms.CharField()
        paymentTerms=forms.CharField()
        discount_presentage=forms.CharField()
        widgets={
            'employeeid':forms.TextInput(attrs={'id':'employeeid',"type":"hidden",})
            
        }
