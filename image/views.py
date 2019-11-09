from django.shortcuts import render
from .models import *
from rest_framework.generics import  ListAPIView
from .serializer import *
from rest_framework.response import Response
from .utils import *
from PIL import Image
import pytesseract
import os



class ImageViewSet(ListAPIView):
    queryset = UploadImageTest.objects.all()
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        print()
        print(request)
        print()
        print(request.data)
        print()

        print(request.data['image'])
        print()
        

        file = request.data['image']
        image = UploadImageTest.objects.create(image=file)
        queryset = UploadImageTest.objects.all()
        
        print(image.image.url)
        print()
        text = pytesseract.image_to_string(Image.open(image.image.url))
        print(text)
        return Response({"GOOD"})