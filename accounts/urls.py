from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', csrf_exempt(views.RegistrationView.as_view()), name="register"),
    path('login',csrf_exempt(views.LoginView.as_view()),name="login"),
    path('add',csrf_exempt(views.AddView.as_view()),name='add'),
    path('logout', views.LogoutView.as_view(), name="logout"),
    path('edit/<int:id>', csrf_exempt(views.EditView.as_view()), name="edit"),
    path('delete/<int:id>', views.DeleteView.as_view(), name="delete"),
    path('view',views.LookView.as_view(),name='view')
]