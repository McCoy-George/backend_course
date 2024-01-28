from django.urls import path
from onlineshope.views import OrderView

urlpatterns = [
    
    path('order/', OrderView.as_view(), name='order'),
]

#Swagger is a framework for describing and documenting
#restful API, it provides a standard way of documentating
#the API in points requests ar responses payload and all
#the details about the API and generates interactive documentation
#that can be used for testing and exploration