from django.urls import path
from .views import InconeList, IncomeDetail

urlpatterns = [
    path('', InconeList.as_view(), name='income'),
    path('<pk:id>/', IncomeDetail.as_view(), name='income-detail')
]
