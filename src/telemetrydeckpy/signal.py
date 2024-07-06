class Signal:

    def __init__(self, app_id, client_user, signal_type, session_id=None, is_test_mode=False, payload=None):
        self.app_id = app_id
        self.client_user = client_user
        self.signal_type = signal_type
        self._session_id = session_id
        self._is_test_mode = is_test_mode
        self._payload = None

    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, new_session_id):
        self._session_id = new_session_id

    @property
    def is_test_mode(self):
        return self._is_test_mode

    @is_test_mode.setter
    def is_test_mode(self, new_is_test_mode):
        self._is_test_mode = new_is_test_mode

    @property
    def payload(self):
        return self._payload

    @payload.setter
    def payload(self, new_payload):
        self._payload = new_payload
