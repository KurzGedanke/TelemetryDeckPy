# TelemetryDeckPy

[TelemetryDeck](https://telemetrydeck.com) is a privacy focuesd user analytics tool. **TelemetryDeckPy** is a small python package to send signals to TelemetryDeck in a pythonic way.

## Usage

```python
def main():
    # Create a telemetrydeckpy object
    telemetry = telemetrydeckpy.TelemetryDeck()
    
    # and a telemetrydeckpy signal object based on 
    # the official documentation
    # https://telemetrydeck.com/docs/ingest/v2/
    signal = telemetrydeckpy.Signal('app_id', 'client_user', 'signal_type')
    
    # and modify it to your own extend
    signal.is_test_mode = True
    signal.payload = {'pay': 'load'}

    # send the signal
    telemetry.send_signal(signal)
```