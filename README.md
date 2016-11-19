# vuplus-mqtt-plugin

This is a very basic plugin for the Vu+. It has been tested with VTi on the vuzero. Currently only the Standby status is reported via MQTT to the broker.

## Install

**Install paho mqtt**

There is no pip installed on the box. This plugin uses the paho mqtt package for python. This has no dependencies. To install it download it from github: https://github.com/eclipse/paho.mqtt.python

Copy the folder /src/paho to /usr/lib/python2.7/site-packages/ on the box.


**Install plugin**

Copy the Mqtt directory fro this repository to /usr/lib/enigma2/python/Plugins/Extensions/

**Adopt the code**

The plugin uses a SSL Client certificate to connect to the broker. If that is not required then simple change the following function accordingly

```
def publishMessage(payload):
    tls = {
        'ca_certs':"/usr/lib/enigma2/python/Plugins/Extensions/Mqtt/ca-certificates.crt",
        'certfile':"/usr/lib/enigma2/python/Plugins/Extensions/Mqtt/mqtt.crt",
        'keyfile':"/usr/lib/enigma2/python/Plugins/Extensions/Mqtt/mqtt.key",
        'tls_version':ssl.PROTOCOL_TLSv1
    }
    try:
        publish.single("/vuzero/standby", payload, retain=False, hostname="mqtt", port=8883, tls=tls)
    except Exception:
        pass
```
