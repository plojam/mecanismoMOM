import pymqi
queue_manager = 'armom'
channel = 'SYSTEM.DEF.SVRCONN'
host = '127.0.0.1'
port = '1414'
conn_info = '%s(%s)' % (host, port)

msg= 'Mi primer mensaje = hola mundo x3'


qmgr = pymqi.connect(queue_manager, channel, conn_info)
putq = pymqi.Queue(qmgr, 'DEV.QUEUE.1')
putq.put(msg)

putq.close()

qmgr.disconnect()

print('Se envio el siguiente mensaje: ', msg)