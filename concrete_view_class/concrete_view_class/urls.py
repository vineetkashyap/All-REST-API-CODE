
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu/',views.MyList.as_view()),
    path('stu1/',views.MyList1.as_view()),
    path('stu2/<int:pk>',views.MyList2.as_view()),
    path('stu3/<int:pk>',views.MyList3.as_view()),
    path('stu4/<int:pk>',views.MyList4.as_view()),
]
