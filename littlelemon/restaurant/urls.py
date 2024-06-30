from django.urls import path, include
from . import views

# Create a router and register our ViewSets with it.

# router.register(r'menu', views.MenuItemView, basename='menu')


urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    # path('booking/', include(router.urls)),
]

