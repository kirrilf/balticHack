from django.shortcuts import render
from .models import *
from rest_framework.generics import  ListAPIView
from .serializer import *
from rest_framework.response import Response
from .utils import *
from PIL import Image
import pytesseract
import os
import cv2



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

        image = image.image.url 

        preprocess = "thresh"

# загрузить образ и преобразовать его в оттенки серого
        image = cv2.imread(image)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # проверьте, следует ли применять пороговое значение для предварительной обработки изображения

        if preprocess == "thresh":
            gray = cv2.threshold(gray, 0, 255,
                cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        # если нужно медианное размытие, чтобы удалить шум
        elif preprocess == "blur":
            gray = cv2.medianBlur(gray, 3)

        # сохраним временную картинку в оттенках серого, чтобы можно было применить к ней OCR

        filename = "{}.png".format(os.getpid())
        cv2.imwrite(filename, gray)
        
        # загрузка изображения в виде объекта image Pillow, применение OCR, а затем удаление временного файла
        text = pytesseract.image_to_string(Image.open(filename))
        os.remove(filename)
        print(text)

        return Response({"GOOD"})