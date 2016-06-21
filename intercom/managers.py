import threading
from contextlib import contextmanager


@contextmanager
def intercom_account(app_id, app_api_key):
    with threading.Lock():
        try:
            from intercom import Intercom
            previous_app_id = Intercom.app_id
            previous_app_api_key = Intercom.app_api_key

            Intercom.app_id = app_id
            Intercom.app_api_key = app_api_key
            yield
        finally:
            Intercom.app_id = previous_app_id
            Intercom.app_api_key = previous_app_api_key
