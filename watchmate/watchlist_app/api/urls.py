from rest_framework.routers import DefaultRouter

from django.urls import path, include
from watchlist_app.api import views

router = DefaultRouter()
router.register('stream', views.StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', views.WatchDetailAV.as_view(), name="movie-detail"),
    
    path('', include(router.urls)),
    # path('stream/', views.StreamPlatformListAV.as_view(), name='stream-list'),
    # path('stream/<int:pk>/', views.StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),

    path('<int:pk>/review-create/', views.ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', views.ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),

    # path('review/', views.ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),
]