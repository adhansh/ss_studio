import socket
from _thread import *

import enums

class SSSocket:
    "통신 소켓"
    
    client_sockets = [] # 서버에 접속한 클라이언트 목록
    # 서버 IP 및 열어줄 포트
    HOST = '192.168.0.14'
    PORT = 9999
    
    bIsStop = False
    
    def StartServer(self):
        # 서버 소켓 생성
        print('>> Server Start')
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.HOST, self.PORT))
        server_socket.listen()

        try:
            while (False == self.bIsStop):
                print('>> Wait')

                client_socket, addr = server_socket.accept()
                self.client_sockets.append(client_socket)
                start_new_thread(self.CommThread, (client_socket, addr))
                print("참가자 수 : ", len(self.client_sockets))
                
        except Exception as e :
            print ('에러는? : ',e)

        finally:
            server_socket.close()
        
        
    
    def CommThread(self, client_socket, addr):
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
                for client in self.client_scokets :
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

        if client_socket in self.client_sockets :
            self.client_sockets.remove(client_socket)
            print('remove client list : ',len(self.client_sockets))

        client_socket.close()
        
#https://kimyhcj.tistory.com/250 참고
class SSProtocol:
    "각 프로토콜의 핸들러를 딕셔너리로 가지고있음"
    dFunc = {}
    
    def SetJobHandler(self, cmd, func):
        self.dFunc[cmd] = func
        
    def DoCmdJob(self, cmd):
        if self.dFunc.get(cmd):
            self.dFunc[cmd]()
        else:
            print('not exsist')
        

def testfunc():
    print('test func')
    
if __name__=='__main__':
    test = SSProtocol();
    
    test.SetJobHandler(1, testfunc)
    test.DoCmdJob(1)
    test.DoCmdJob(2)
    