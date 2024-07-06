import json
import logging

from requests import Request, Session


def serialise_payload(signal) -> dict:
    payload = {
        'appID': signal.app_id,
        'clientUser': signal.client_user,
        'type': signal.signal_type,
        'isTestMode': str(signal.is_test_mode).lower(),
    }

    if signal.session_id:
        payload.update({'sessionID': signal.session_id})

    if signal.payload:
        payload.update({'payload': signal.payload})

    return payload


class TelemetryDeck:

    def __init__(self):
        pass

    def send_signal(self, signal):
        url = 'https://nom.telemetrydeck.com/v2/'
        s = Session()

        headers = {
            'Content-Type': 'application/json; charset=utf-8',
        }

        req = Request('POST', url, data=json.JSONEncoder().encode([serialise_payload(signal)]), headers=headers)
        try:
            resp = s.send(req.prepare())
        except Exception as e:
            logging.error(e)
