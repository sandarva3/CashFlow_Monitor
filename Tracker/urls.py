from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from Trace.views import (
    home_screen_view,
    guestHome_view,
    whole_view,
    wholeadd_view,
    add_view,
    guestAdd_view,
    remove_view,
    Wremove_view,
    login_view,
    register_view,
    logout_view,
)

urlpatterns = [
    path('', guestHome_view, name="guestHome"),
    path('events/', include('events.urls')),
    path('wholething/', whole_view, name="wholething"),
    path('wholeadd/', wholeadd_view, name="wholeadd"),
    path('admin/', admin.site.urls),
    path('register/', register_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('add/', add_view, name="add"),
    path("guestadd/", guestAdd_view, name="guestAdd"),
    path('slug:<username>/', home_screen_view, name="home"),
    path('remove/<int:id>', remove_view, name="remove"),
    path('Wremove/<int:id>', Wremove_view, name="Wremove"),
    path('accounts/', include('allauth.urls')),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='register_confirm'),

    path('account/confirm/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/register_email.html'),
     name='register_email')
    
]