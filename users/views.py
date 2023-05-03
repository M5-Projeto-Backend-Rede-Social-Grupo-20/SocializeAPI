from django.shortcuts import render
from .models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = "id"

# Create your views here.

# class UserView(RetrieveModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     lookup_url_kwarg = "id"

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class UserDetailView(ListModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     lookup_url_kwarg = "id"

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def update(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def destroy(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
