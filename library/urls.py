
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('home.urls', 'home'), namespace='home')),
    path('books/', include(('books.urls', 'books'), namespace='books')),
    path('takenBooks/', include(('takenBooks.urls', 'takenBooks'), namespace='takenBooks')),
]
