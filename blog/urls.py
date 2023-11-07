from . import views
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [

    path('autores', views.AutorList.as_view()),
    path('autores/<int:pk>', views.AutorDetail.as_view()),
    path('autores/create', views.AutorCreate.as_view()),
    path('autores/<int:pk>/update', views.AutorUpdate.as_view()),
    path('autores/<int:pk>/delete', views.AutorDelete.as_view()),

    path('posts', views.PostList.as_view()),
    path('posts/<int:pk>', views.PostDetail.as_view()),
    path('posts/create', views.PostCreate.as_view()),
    path('posts/<int:pk>/update', views.PostUpdate.as_view()),
    path('posts/<int:pk>/delete', views.PostDelete.as_view()),

    path('comentarios', views.ComentarioList.as_view()),
    path('comentarios/<int:pk>', views.ComentarioDetail.as_view()),
    path('comentarios/create', views.ComentarioCreate.as_view()),
    path('comentarios/<int:pk>/update', views.ComentarioUpdate.as_view()),
    path('comentarios/<int:pk>/delete', views.ComentarioDelete.as_view()),

    path('token', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
]
