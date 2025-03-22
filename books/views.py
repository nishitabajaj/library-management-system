from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # GET (safe methods) sabke liye allow, but POST/PUT/DELETE only for admin
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

# GET (List) & POST (Create)
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]

# GET (Retrieve), PUT (Update), DELETE (Delete)
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]
