import time


def cfan(var):
    varOSD = 'OSD_false'
    boolIntent = 'INTENT_true'
    varINTENT = 'com.auto.Coolerfan.' + var
    varExtra = ''
    varActName = 'Cooler fan ' + var
    millis = str(int(round(time.time() * 1000)))
    print
    millis
    eg.plugins.AutoRemote.SendMessage(u'Xiomi', u'goo.gl/FYt2fV',
                                      u'APA91bGwgMNFCvt7kRLppZCpDiXkNUw4r2YAd62SXAknUNITIrTdoxKRTc6U8AeIDZFv0k---zf3R8OZtQocxvdbKTX0JRKrxxOKAFoINqnSh0395WUm24Sv-3q5qIlChrkruWFpzcCQ',
                                      millis + u" " + varOSD + " " + boolIntent + " " + varINTENT + u"=:=" + varExtra,
                                      u'', u'YC6W7ypr8*88Y!bG', u'', '', u'', u'')
    # eg.plugins.EventGhost.ShowOSD(u'Finding Xiomi_Android', u'0;-24;0;0;0;700;0;0;0;1;0;0;2;32;Arial', (255, 255, 255), (0, 0, 0), 0, (0, 0), 0, 3.0, False)
    eg.globals.PendingAction.append([millis, varActName])


# cfan('off')

def sendTCP(var):
    import socket
    target = '192.168.1.251'
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target, 80))
    client.send(var)


if eg.globals.roomcoolerState:
    # cfan('off')
    sendTCP("*##AUTO_OFF##*")
    sendTCP("*##CFAN_OFF##*")
    eg.globals.roomcoolerState = False

else:
    # cfan('on')
    sendTCP("*##AUTO_OFF##*")
    sendTCP("*##CFAN_ON##*")
    eg.globals.roomcoolerState = True


