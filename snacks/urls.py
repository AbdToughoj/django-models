from django.urls import path
from .views import Snack_List_View

urlpatterns = [
    path('', Snack_List_View.as_view(), name= 'Snack List' )
]
