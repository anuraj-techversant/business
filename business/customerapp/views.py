"""
The views.py contains functions to perform codes based on various http requests
"""
from customerapp.models import Customer
from customerapp.serializers import CustomerSerializer
from customerapp.permissions import IsAuthenticatedUser
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


class CustomerView(generics.ListCreateAPIView):
    """
    The view handles the GET and POST request for listing all 
    customer data and creation of customer.
    """
    permission_classes = [IsAuthenticatedUser]
    serializer_class = CustomerSerializer

    def get_queryset(self):
        """
        List all customer data from Customer model. 
        """
        customer_objs = Customer.objects.all()
        return customer_objs

    def post(self, request, format=None):
        """
        Create a new entry for customer in Customer model.
        """
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": status.HTTP_201_CREATED, 
                "message": "Customer created succesfully", 'data': serializer.data})
        return Response({"status": status.HTTP_400_BAD_REQUEST, 
            "message": "Customer creation failed", "data": serializer.errors})


class CustomerDescriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    The view handles the GET, PUT and DELETE request for list a particular entry of 
    customer data, Edit a customer entry, Delete a customer entry.
    """
    permission_classes = [IsAuthenticatedUser]
    serializer_class = CustomerSerializer

    def get(self, request, pk, format=None):
        """
        List a customer entry from Customer model. 
        """
        details = None
        try:
            details = Customer.objects.get(id=pk)
        except:
            return Response({'status': status.HTTP_404_NOT_FOUND, 
                'message': "Customer detail not found"})
        serializer = CustomerSerializer(details)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        Edit fields of a customer entry from Customer model. 
        """
        details = None
        try:
            details = Customer.objects.get(id=pk)
        except:
            return Response({'status': status.HTTP_404_NOT_FOUND, 
                'message': "Customer detail not found"})
        serializer = CustomerSerializer(details, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': status.HTTP_200_OK, 
                'message': "Customer details updated successfully", 'data': serializer.data})
        return Response({'status': status.HTTP_400_BAD_REQUEST, 
            'message': "Customer details updation failed", 'data': serializer.errors})

    def delete(self, request, pk, format=None):
        """
        Delete a customer entry from Customer model. 
        """
        try:
            if Customer.objects.filter(id=pk).exists():
                details = Customer.objects.get(id=pk)
                details.delete()
                return Response({'status': status.HTTP_200_OK, 
                    'message': "Customer detail deleted successfully"})
            else:
                return Response({'status': status.HTTP_404_NOT_FOUND, 
                    'message': "Customer detail not found"})
        except:
            return Response({'status': status.HTTP_400_BAD_REQUEST, 
                'message': "Customer detail deletion failed"})
