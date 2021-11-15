import pymqi

queue_manager = 'armom'
channel = 'SYSTEM.DEF.SVRCONN'
host = '127.0.0.1'
port = '1414'
conn_info = '%s(%s)' % (host, port)

qmgr = pymqi.connect(queue_manager, channel, conn_info)
getq = pymqi.Queue(qmgr, 'DEV.QUEUE.1')
print('Here is the message:', getq.get())