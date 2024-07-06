import telemetrydeckpy


def test_telemetrydeck():
    telemetry = telemetrydeckpy.TelemetryDeck()
    signal = telemetrydeckpy.Signal('app_id', 'client_user', 'signal_type')
    signal.is_test_mode = True
    signal.payload = {'pay': 'load'}

    telemetry.send_signal(signal)
