from typing import Iterable

from adapters import file_transfer
from adapters.emailing.emailing_settings import EmailingSettings
from camera_ctrl.models.app_settings_models import GeneralSettings


class SettingsFacade(EmailingSettings, file_transfer.notifications_settings.NotificationsSettings):
    @property
    def send_email_on_capture_error(self) -> bool:
        return GeneralSettings.get().send_email_on_capture_error

    @property
    def send_email_on_timelapse_error(self) -> bool:
        return GeneralSettings.get().send_email_on_timelapse_error

    @property
    def send_email_on_sync_error(self) -> bool:
        return GeneralSettings.get().send_email_on_sync_error

    @property
    def emails(self) -> Iterable[str]:
        return GeneralSettings.get().emails.split()

    @property
    def email_subject_prefix(self) -> str:
        return GeneralSettings.get().email_subject_prefix

    @property
    def seconds_to_wait_after_hard_reset(self) -> int:
        return GeneralSettings.get().seconds_to_wait_after_hard_reset

    @property
    def hard_reset_on_timelapse_error(self) -> bool:
        return GeneralSettings.get().hard_reset_on_timelapse_error

    @property
    def log_to_db_camera_capture(self) -> bool:
        return GeneralSettings.get().log_to_db_camera_capture

    @property
    def persistent_log_on_file_transferred(self):
        return True

    @property
    def autodetect_cameras_on_start(self) -> bool:
        return GeneralSettings.get().autodetect_cameras_on_start
