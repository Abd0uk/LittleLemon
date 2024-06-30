from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework import viewsets
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated


# Used for homepage
def index(request):
    return render(request, 'index.html', {})

#? Menu Model Views

class MenuItemView(ListCreateAPIView): # POST & GET Methods calls.
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView): # GET, PUT and DELETE calls.
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


#? Booking Model Views

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]