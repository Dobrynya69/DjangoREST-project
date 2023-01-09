from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import Image
from rest_framework import status
from .serializers import ImageSerializer
from .permitions import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination


class ImageAPIPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = "custom_size"
    max_page_size = 100


class ImageViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, isAuthorOrReadOnly]
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    pagination_class= ImageAPIPagination


    @action(methods=['post'], detail=False)
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer = self.serializer_class(Image.objects.create(title=data['title'], image=data['image'], author=request.user))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Data is not valid!"}, status=status.HTTP_400_BAD_REQUEST)


    @action(methods=['get'], detail=False)
    def images(self, request):
        images = ['http://' + request.META['HTTP_HOST'] + image.image.url for image in self.get_queryset()]
        return Response(images, status=status.HTTP_202_ACCEPTED)





"""
class ImagesView(APIView):
    serializer_class = ImageSerializer


    def get(self, request):
        images = Image.objects.all()
        return Response(self.serializer_class(images, many=True).data, status=status.HTTP_202_ACCEPTED)
    

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer = self.serializer_class(Image.objects.create(title=data['title'], image=data['image'], author=request.user))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Data is not valid!"}, status=status.HTTP_400_BAD_REQUEST)


class ImageDetailView(APIView):
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated, isAuthorOrReadOnly]

    def get(self, request, *args, **kwargs):
        try:
            image = Image.objects.get(slug=kwargs['slug'])
        except Image.DoesNotExist:
            return Response({"message": "Image does not exist!"}, status=status.HTTP_204_NO_CONTENT)
        return Response(self.serializer_class(image).data, status=status.HTTP_202_ACCEPTED)

    
    def delete(self, request, *args, **kwargs):
        try:
            Image.objects.get(slug=kwargs['slug']).delete()
        except Image.DoesNotExist:
            return Response({"message": "Delete error. Image does not exist!"}, status=status.HTTP_400_BAD_REQUEST)
            
        return Response({"message": "Delete was success!"}, status=status.HTTP_202_ACCEPTED)


    def put(self, request, *args, **kwargs):
        try:
            image = Image.objects.get(slug=kwargs['slug'])
        except Image.DoesNotExist:
            return Response({"message": "Image does not exist!"}, status=status.HTTP_204_NO_CONTENT)
            
        serializer = self.serializer_class(image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Data is not valid!"}, status=status.HTTP_400_BAD_REQUEST)

    
    def patch(self, request, *args, **kwargs):
        try:
            image = Image.objects.get(slug=kwargs['slug'])
        except Image.DoesNotExist:
            return Response({"message": "Image does not exist!"}, status=status.HTTP_204_NO_CONTENT)
            
        serializer = self.serializer_class(image, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Data is not valid!"}, status=status.HTTP_400_BAD_REQUEST)
"""