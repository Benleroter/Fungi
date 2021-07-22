from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from fungi import views
from fungi.views import FungiDetail
from fungi.views.search import Search
from users  import views as user_views
from django.contrib.auth import views as auth_views
#from usersettings.views import (CreateFilter,FilterView,EditFilter)
from usersettings.views import (EditFilter)
import debug_toolbar

admin.autodiscover()
admin.site.enable_nav_sidebar = False

app_name = 'fungi'

urlpatterns = [
    path('', views.home, name='AllFungi-HomePage'),
    path('allfungi', views.AllFungi, name='AllFungiList'),
    path('about/', views.about, name='AllFungi-AboutPage'),
    path('home/', views.home, name='AllFungi-HomePage'),
    path('detail/<int:pk>/', FungiDetail.as_view(), name='FungiDetail-Page'),
	path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
	path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('admin/', admin.site.urls, name='admin'),

    #PASSWORD
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
    path('usersettings/', include('usersettings.urls', namespace="usersettings")),
    
    #SEARCH
    path('searchresults/', Search, name='search-fungi'),
    path('searchsuccess/', views.searchsuccess, name='search-success'),
    path('nosearchresults/', views.nosearchresults, name='no-search-results'),

    path('__debug__/', include(debug_toolbar.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()