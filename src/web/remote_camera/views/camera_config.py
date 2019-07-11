from business.CameraManager import CameraManager
from business.CameraWrapper import CameraWrapper, CameraConfig
from django.shortcuts import render

from .camera_not_found import camera_not_found
from ..forms import CameraConfigForm


def camera_config(request, camera_port):
    camera = CameraManager.instance().get_camera_on_port(camera_port)
    if camera is None:
        return camera_not_found(request, camera_port)

    assert isinstance(camera, CameraWrapper)

    config = camera.get_config()
    config_form = CameraConfigForm(config)
    context = {
        'camera_port': camera_port,
        'form': config_form,
    }

    return render(request, 'remote_camera/camera_config.html', context)


def apply_config_changes(camera, camera_configs, values):
    assert isinstance(camera, CameraWrapper)

    config_changed = False
    for section in camera_configs:
        assert isinstance(section, CameraConfig)

        for config in section.child_configs:
            assert isinstance(section, CameraConfig)

            field_name = '{0}/{1}'.format(section.name, config.name)
            if field_name not in values:
                continue

            value = values[field_name]

            if config.value != value:
                config.set_value(value)
                config_changed = True

    if not config_changed:
        return



