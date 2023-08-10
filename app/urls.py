from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.AddBook.as_view()),
    path('category',views.AddCategory.as_view()),

    path('category/<int:id>/',views.EditCategoryCBV.as_view()),
    path('book/<int:id>/',views.EditBookCBV.as_view()),

]