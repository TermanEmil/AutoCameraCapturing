from django.urls import path

from shared.utils.setup_startup import setup_startup
from .factories import *


setup_startup(lambda: startup_factory().run())

urlpatterns = [
    path('', index_view_factory(), name='index'),
    path('index', index_view_factory(), name='index'),
    path('single_preview/<str:camera_id>', single_preview_view_factory(), name='single_preview'),
    path('multi_preview', multi_preview_view_factory(), name='multi_preview'),

    path('api/cameras_autodetect', cameras_autodetect_view_factory(), name='api/cameras_autodetect'),
    path('api/camera_remove/<str:camera_id>', camera_remove_view_factory()),
    path('api/camera_reconnect/<str:camera_id>', camera_reconnect_view_factory()),
    path('api/camera_preview_source/<str:camera_id>', camera_preview_source_factory(), name='api/camera_preview_source'),
    path('api/cameras_hard_reset_all', cameras_hard_reset_all(), name='api/cameras_hard_reset_all'),

    path(
        'api/camera_capture_img_and_download/<str:camera_id>',
        camera_capture_img_and_download_factory(),
        name='camera_capture_img_and_download'),
]
