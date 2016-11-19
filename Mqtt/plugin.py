from Plugins.Plugin import PluginDescriptor
from Screens import Standby
from Components.config import config
import paho.mqtt.publish as publish
import ssl


def main(reason, **kwargs):
    print "\n<<<<<<<<<< Reason: {} >>>>>>>>>>\n".format(reason)
    config.misc.standbyCounter.addNotifier(enterStandby, initial_call = False)
    
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

def enterStandby(configElement):
    print "Entering Standby Mode"
    publishMessage(0)
    Standby.inStandby.onClose.append(endStandby)
    
def endStandby():
    print "Exiting Standby Mode"
    publishMessage(1)
    
def Plugins(**kwargs):
    return PluginDescriptor(
        where = PluginDescriptor.WHERE_AUTOSTART,
        fnc=main)
