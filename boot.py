import gc
import esp
import network

ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

gc.collect()
esp.osdebug(None)
