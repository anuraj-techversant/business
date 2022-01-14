
from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from customerapp.permissions import IsAuthenticatedUser
from customerapp.models import customer
from customerapp.serializers import CustomerSerializer

class CustomerView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedUser]
    serializer_class = CustomerSerializer

    def get_queryset(self):
        customer_objs = customer.objects.all()
        return customer_objs

    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": status.HTTP_201_CREATED, "message": "Customer created succesfully", 'data': serializer.data})
        return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "Customer creation failed", "data": serializer.errors})


class CustomerDescriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedUser]
    serializer_class = CustomerSerializer

    def get(self, request, pk, format=None):
        details = None
        try:
            details = customer.objects.get(id=pk)
        except:
            return Response({'status': status.HTTP_404_NOT_FOUND, 'message': "Customer detail not found"})
        serializer = CustomerSerializer(details)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        details = None
        try:
            details = customer.objects.get(id=pk)
        except:
            return Response({'status': status.HTTP_404_NOT_FOUND, 'message': "Customer detail not found"})
        serializer = CustomerSerializer(details, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': status.HTTP_200_OK, 'message': "Customer details updated successfully", 'data': serializer.data})
        return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': "Customer details updation failed", 'data': serializer.errors})

    def delete(self, request, pk, format=None):
        try:
            if customer.objects.filter(id=pk).exists():
                details = customer.objects.get(id=pk)
                details.delete()
                return Response({'status': status.HTTP_200_OK, 'message': "Customer detail deleted successfully"})
            else:
                return Response({'status': status.HTTP_404_NOT_FOUND, 'message': "Customer detail not found"})
        except:
            return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': "Customer detail deletion failed"})

