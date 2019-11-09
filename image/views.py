from django.shortcuts import render
from .models import *
from rest_framework.generics import  ListAPIView
from .serializer import *
from rest_framework.response import Response

class ImageViewSet(ListAPIView):
    queryset = UploadImageTest.objects.all()
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        print()
        print(request)
        print()
        print(request.data)
        print()

        file = request.data['image']
        image = UploadImageTest.objects.create(image=file)
        return Response({"GOOD"})