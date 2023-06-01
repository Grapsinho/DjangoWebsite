from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('playground.urls')),
    path('', include('users.urls'))
]

#ანუ ჩვენ იმ ორ რაღაცას ვაკავშირებთ რაც სეთინგებში გავწერეთ ფოტოსთვის
#ფაილ path იქნება ის პირველი ურლ ხოლო ფაილებს მივიღებთ მეორედან რუთიდან
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)