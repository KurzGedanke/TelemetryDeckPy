import telemetrydeckpy


def test_signal():
    signal = telemetrydeckpy.Signal('app_id', 'client_user', 'signal_type')

    assert signal.app_id == 'app_id'
    assert signal.client_user == 'client_user'
    assert signal.signal_type == 'signal_type'

    assert signal.session_id is None
    assert signal.is_test_mode is False
    assert signal.payload is None

    signal.session_id = 'session_id'
    signal.is_test_mode = True
    signal.payload = {"pay": "load"}

    assert signal.session_id == 'session_id'
    assert signal.is_test_mode is True
    assert signal.payload == {"pay": "load"}
