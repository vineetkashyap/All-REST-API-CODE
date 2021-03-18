
from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("get/",views.MyList.as_view()),
    path("create/",views.MyCreate.as_view()),
    path("update/<int:pk>",views.MyUpdate.as_view()),
    path("retrieve/<int:pk>",views.MyRetrieve.as_view()),
    path("delete/<int:pk>",views.MyDelete.as_view()),
]
