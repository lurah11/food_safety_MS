from django.db import models
from django.urls import reverse

# Create your models here.

class Customer(models.Model): 
    STATUS_CHOICE = [
        ('Mass Production','MP'),
        ('Trial','T'),
        ('Inactive','I')
    ]
    name = models.CharField(max_length=100)
    brands = models.CharField(max_length=200)
    status = models.CharField(choices=STATUS_CHOICE,max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self): 
        return f"Customer__{self.name}"
    def get_absolute_url(self): 
        return reverse('customer-detail-view',kwargs={'pk':self.pk})

class Product(models.Model):
    TYPE_CHOICE = [
        ('Coffee Drink','Coffee Drink'),
        ('Tea Drink','Tea Drink'),
        ('Flavored Drink','Flavored Drink'),
        ('Botanical Drink','Botanical Drink'),
        ('Isotonic Drink','Isotonic Drink'),
        ('Soya Drink','Soya Drink')
    ]
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    legal_name = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    volume = models.CharField(max_length=100)
    type = models.CharField(choices=TYPE_CHOICE,default='Tea', max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    domestic_distribution = models.BooleanField(default=True)
    export_distribution = models.BooleanField(default=False)
    remark = models.CharField(max_length=300,null=True,blank=True)

    def __str__(self) -> str:
        return f"Product__{self.brand}-{self.name}-{self.volume}"
    def get_absolute_url(self): 
        return reverse('product-detail-view',kwargs={'pk':self.pk})

class ProductionLine(models.Model): 
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    line = models.IntegerField()

    def __str__(self): 
        return f"Product__{self.brand}-{self.name}-line {self.line}{self.volume}"

class ProductionInstance(models.Model): 
    product_line = models.ForeignKey(ProductionLine,on_delete=models.SET_NULL)
    prod_cycle_start = models.DateField()
    prod_cycle_end = models.DateField()
    quantity = models.IntegerField()






