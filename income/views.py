from django.shortcuts import render
from .serializers import IncomeSerializer
from .models import Income
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsOwner
# Create your views here.


class InconeList(ListCreateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = (IsOwner, )
    lookup_field = 'id'


    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class IncomeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = (IsOwner, )


    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)