from django.db import models


class Machine(models.Model):
    name = models.CharField(max_length=30,blank=True,null=True,default='')

    def __str__(self):
        if self.name == None:
            return "ERROR-MACHINE MNAME IS NULL"
        return self.name

    class Meta:
        verbose_name_plural = 'Machine'    

class Type(models.Model):
    name = models.CharField(max_length=30,blank=True,null=True,default='0')

    def __str__(self):
        if self.name == None:
            return "ERROR-TYPE TNAME IS NULL"
        return self.name

    class Meta:
        verbose_name_plural = 'Type'



class Coffee_Pod(models.Model):
    name = models.CharField(max_length=50,blank=True,null=True,default='')

    def __str__(self):
        if self.name == None:
            return "ERROR-COFFEEPOD CNAME IS NULL"
        return self.name

    class Meta:
        verbose_name_plural = 'Coffee_Pod' 


class Flavour(models.Model):
    name = models.CharField(max_length=30,blank=True,null=True,default='')

    def __str__(self):
        if self.name == None:
            return "ERROR-FLAVOUR NAME IS NULL"
        return self.name

    class Meta:
        verbose_name_plural = 'Flavour' 


class WL(models.Model):
    name = models.CharField(max_length=30,blank=True,null=True,default='')

    def __str__(self):
        if self.name == None:
            return "ERROR-WATERLINE WNAME IS NULL"
        return self.name

    class Meta:
        verbose_name_plural = 'WL'   


class PackSize(models.Model):
    name = models.CharField(max_length=30,blank=True,null=True,default='')

    def __str__(self):
        if self.name == None:
            return "ERROR-PACKSIZE PNAME IS NULL"
        return self.name

    class Meta:
        verbose_name_plural = 'PackSize'                       

class Category(models.Model):
    option = models.CharField(max_length=300,blank=True,null=True)
    machine = models.ForeignKey(Machine, on_delete=models.SET_NULL, null=True,blank=True,default='0')
    flavour = models.ForeignKey(Flavour, on_delete=models.SET_NULL, null=True,blank=True,default='0')
    coffeePod = models.ForeignKey(Coffee_Pod, on_delete=models.SET_NULL, null=True,blank=True,default='0')
    Type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True,blank=True,default='0')
    packsize = models.ForeignKey(PackSize, on_delete=models.SET_NULL, null=True,blank=True,default='0')
    wl = models.ForeignKey(WL, on_delete=models.SET_NULL, null=True,blank=True,default='0')


    def __str__(self):
        if self.option == None:
            return "ERROR-CATEGORY CatNAME IS NULL"
        return self.option

    class Meta:
        verbose_name_plural = 'Category'   
    
