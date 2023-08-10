
# import libraries
from .models import Book,Category
from .serializers import BookSerialser, CategorySerializer
from rest_framework import mixins, generics, viewsets, filters


# CBV for add books
class AddBook (mixins.ListModelMixin, generics.GenericAPIView,mixins.CreateModelMixin) :
    queryset = Book.objects.all()
    serializer_class = BookSerialser
    
    def get(self, request) :
        return self.list(request)

    def post(self, request) :
        return self.create(request)
    


# CBV for add categories
class AddCategory (mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView) :
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self,request):
        return self.list(request)
    
    def post (self,request) :
        return self.create(request)



# CBV for work on categories
class EditCategoryCBV (mixins.RetrieveModelMixin,mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView) :
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 
    lookup_field = 'id'
    def get (self, request, id) :
        return self.retrieve(request)
    def put (self,request, id) :
        return self.update(request)
    def delete (self, request, id) :
        return self.destroy(request)
    



# CBV for work on books
class EditBookCBV (mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView) :
    
    queryset = Book.objects.all()
    serializer_class = BookSerialser
    lookup_field = 'id'

    def get (self, request, id) :
        return self.retrieve(request)

    def put (self,request,id) :
        return self.update(request)
    
    def delete (self,request, id) :
        return self.destroy(request)
    

# CBV for using viewsets with category model
class CategoryViewSet (viewsets.ModelViewSet) :
    
    # default parameters
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # for search
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


# CBV for using viewsets with book model 
class BookViewSet (viewsets.ModelViewSet) :
    
    # default parameters
    queryset = Book.objects.all()
    serializer_class = BookSerialser


    # for search
    filter_backends = [filters.SearchFilter]
    search_fileds = ['name']
