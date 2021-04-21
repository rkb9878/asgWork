from django.urls import path, include
from manageAPI.api import view
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

app_name = 'manageAPI'

router = DefaultRouter()
router.register('BusinessView', view.BusinessView)
router.register('ProductView', view.ProductView)

urlpatterns = [
    path('', view.indexView, name='indexView'),
    path('register', view.userRegisterView.as_view(), name='register'),
    path('login', obtain_auth_token, name='login'),
    path('manage/', include(router.urls), name='Business'),

]
