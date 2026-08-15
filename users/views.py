from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserProfileSerializer
# Create your views here.

@api_view(['POST'])
def register_user(request):

    serializer = UserProfileSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()

        return Response(
            UserProfileSerializer(user).data,
            status=status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )
