from django.db import models
from base.models import ProductionLine, ProductionInstance

# Create your models here.
class CCPItem(models.Model): 
    prod_line = models.ForeignKey(ProductionLine,on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    tag = models.CharField(max_length=50)
    unit = models.CharField(max_length=20)
    std_max = models.FloatField()
    std_min = models.FloatField()

    def __str__(self): 
        return f"CCP--{self.prod_line.product.brand}_{self.prod_line.product.name}-{self.name}-{self.tag}"

class CCPRecords(models.Model): 
    prod_ins = models.ForeignKey(ProductionInstance,on_delete=models.CASCADE)
    ccp_item = models.ForeignKey(CCPItem,on_delete=models.CASCADE)
    min = models.FloatField(null=True,blank=True)
    max = models.FloatField(null=True,blank=True)
    result = models.CharField(max_length=50)
    remark = models.CharField(max_length=500, null=True,blank=True)
