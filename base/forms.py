from .models import Customer, Product
from django import forms 

# class CustomerForm(forms.ModelForm): 
#     class Meta:
#         model=Customer 
#         fields=['name','brands','status']

class ProductForm(forms.ModelForm): 
    def __init__(self,*args,**kwargs): 
        super().__init__(*args,**kwargs)
        for key in self.fields.keys():
            if key in ["name","legal_name","brand","volume","remark"]:
                self.fields[key].widget.attrs.update(size="70")        
    class Meta: 
        model=Product
        exclude=["created","modified"]

class SearchForm(forms.Form): 
    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['query'].required = False
    query = forms.CharField(max_length=50)

        