from ninja import Router, File
from ninja.files import UploadedFile
from .models import Document
from .utils import calculate_hash


router = Router()

@router.post("/upload", auth=GlobalAuth())
async def upload_document(request, file: File[UploadedFile]):
    pass