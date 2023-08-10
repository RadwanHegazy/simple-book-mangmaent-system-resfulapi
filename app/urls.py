from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


# category router
router = DefaultRouter()
router.register('category',views.CategoryViewSet)
router.register('book',views.BookViewSet)


urlpatterns = [
    
    
    # view data using mixins
    path('',views.AddBook.as_view()),
    path('category',views.AddCategory.as_view()),

    # update and delete data using mixins
    path('category/mixins/<int:id>/',views.EditCategoryCBV.as_view()),
    path('book/mixins/<int:id>/',views.EditBookCBV.as_view()),


    # viewsets for category and books [view, update, delete ]
    path('viewsets/',include(router.urls)),

]