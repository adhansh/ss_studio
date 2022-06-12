import socket
from _thread import *

from camera_switch import *


client_sockets = [] # 서버에 접속한 클라이언트 목록

# 서버 IP 및 열어줄 포트
HOST = '192.168.0.14'
PORT = 9999

global bIsStop

bIsStop = False;

def DoCmdJob(cmd):
    if 'cmd:mono' == cmd:
        print('run cmd(mono)')
        SetPicStyle('mono')
        
        
    elif 'cmd:color' == cmd:
        print('run cmd(color)')
        #SetColor()
        SetPicStyle('color')

# 쓰레드에서 실행되는 코드입니다.
# 접속한 클라이언트마다 새로운 쓰레드가 생성되어 통신을 하게 됩니다.
def threaded(client_socket, addr):
    print('>> Connected by :', addr[0], ':', addr[1])

    # 클라이언트가 접속을 끊을 때 까지 반복합니다.
    while True:
        try:
            # 데이터가 수신되면 클라이언트에 다시 전송합니다.(에코)
            data = client_socket.recv(1024)
            if not data:
                print('>> Disconnected by ' + addr[0], ':', addr[1])
                break
            
            print('>> Received from ' + addr[0], ':', addr[1], data.decode())
            
            # 서버에 접속한 클라이언트들에게 채팅 보내기
            # 메세지를 보낸 본인을 제외한 서버에 접속한 클라이언트에게 메세지 보내기
            for client in client_sockets :
                if client != client_socket :
                    client.send(data)
            
            # 픽쳐스타일 변경 명령인지 검토한다
            recv_msg = str(data.decode())
            if 'cmd:' in recv_msg:
                print('detect cmd : ', recv_msg)
                DoCmdJob(recv_msg)

        except ConnectionResetError as e:
            print('>> Disconnected by ' + addr[0], ':', addr[1])
            break

    if client_socket in client_sockets :
        client_sockets.remove(client_socket)
        print('remove client list : ',len(client_sockets))

    client_socket.close()

def InputThread(n):
    while True:
        x = input('')
        
        if ('q' == x):
            bIsStop = True
            client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            client_socket.connect((HOST, PORT))
            client_socket.close()
            
            break
    
    

def StartServer():
    # 서버 소켓 생성
    print('>> Server Start')
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    try:
        while (False == bIsStop):
            print('>> Wait')

            client_socket, addr = server_socket.accept()
            client_sockets.append(client_socket)
            start_new_thread(threaded, (client_socket, addr))
            print("참가자 수 : ", len(client_sockets))
            
    except Exception as e :
        print ('에러는? : ',e)

    finally:
        server_socket.close()
        
if __name__=='__main__':
    #start_new_thread(InputThread,(__name__,))
    StartServer()