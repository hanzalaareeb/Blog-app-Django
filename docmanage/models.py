from django.db import models
from django.conf import settings
from pgvector.django import VectorField



class Document(models.Model):
    # Link to user/models.py User model
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # MetaData
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    file_type = models.CharField(max_length=10)
    is_public = models.BooleanField(auto_now_add=True)
    
    # deduplication Hash (SHA-256 of the file content)
    content_hash = models.CharField(max_length=64, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
class DocumentChunk(models.Model):
    document = models.ForeignKey(Document, related_name='chunks', on_delete=models.CASCADE)
    content = models.TextField() # actual test segment
    page_number = models.IntegerField(dimensions=1536)