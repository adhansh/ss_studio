import socket
from _thread import *

from camera_switch import *

HOST = '192.168.0.13' #서버주소
PORT = 9999

# 서버로부터 메세지를 받는 메소드
# 스레드로 구동 시켜, 메세지를 보내는 코드와 별개로 작동하도록 처리
def recv_data(client_socket) :
    while True :
        data = client_socket.recv(1024)
        # 픽쳐스타일 변경 명령인지 검토한다
        recv_msg = str(data.decode())
        if 'cmd:' in recv_msg:
            print('detect cmd : ', recv_msg)
            sndData = ''
            if DoCmdJob(recv_msg):
                sndData = 'res:ok'
            else:
                sndData = 'res:fail'
            client_socket.send(sndData.encode())
            
        else:
            print("recive : ",repr(data.decode()))


def StartClient():
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    
    start_new_thread(recv_data, (client_socket,))
    print ('>> Connect Server')

    while True:
        message = input('')
        if message == 'quit':
            close_data = message
            break
        #client_socket.send(message.encode())       
    client_socket.close()
    
if __name__=='__main__':
    StartClient()