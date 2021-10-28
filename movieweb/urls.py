from django.urls import path

from django.contrib.auth import views as auth_views #import this

from movieweb.views.adminview import Adminview, AddAdminview, ViewUser, AddUser

from movieweb.views.loginview import UserLogin
from movieweb.views.movieview import UpdateRating, AddMovie, EditMovie, UpdateMovie
from movieweb.views.resetpassword import ResetPasswordView, UpdatePassword
from movieweb.views.signupview import UserSignUp
from movieweb.views.userview import Userview

urlpatterns = [

    path('', UserSignUp.as_view(), name='sign-up'),
    path('addmovie', AddMovie.as_view(), name='add-movie'),
    path('updatemovie', UpdateMovie.as_view(), name='update-movie'),
    path('updaterating', UpdateRating.as_view(), name='up-rating'),
    path('adduser', AddUser.as_view(), name='adduser'),
    path('login', UserLogin.as_view(), name='login'),
    path('editmovie', EditMovie.as_view(), name='editmovie'),
    path('adminv', Adminview.as_view(), name='adminview'),
    path('userv', Userview.as_view(), name='userview'),
    path('addadmin', AddAdminview.as_view(), name='addadmin'),
    path('viewuser', ViewUser.as_view(), name='viewuser'),
    path('password-reset/', ResetPasswordView, name='password_reset'),
    path('reset/<uidb64>/<str:token>/', UpdatePassword.as_view(template_name="movieweb/password/password_reset_confirm.html"), name='password_reset_confirm'),
]