from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Tag(models.Model):
    label =models.CharField(max_length=255)
    
class TaggedItem(models.Model):
    tag =models.ForeignKey(Tag, on_delete=models.CASCADE)
    
    '''to be able to use any class or models we use django's contenttype app which helps to import any object ( i.e allow generic relations )'''
    
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id=models.PositiveIntegerField()
    #to get the actual prdct the tag is applied to
    content_object = GenericForeignKey()
    