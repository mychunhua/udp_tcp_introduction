from socket import *


def service_client(new_socket, client_addr):
    """用来为这个客户端返回数据"""
    # 接收浏览器的请求
    recv_data = new_socket.recv(1024).decode("utf-8")
    print(str(client_addr[0]) + ":" + recv_data)
    # 给浏览器返回http格式的数据
    header = "HTTP/1.1 200 OK\r\n"  # 浏览器中\r\n表示换行
    header += "\r\n"
    body = "hahaha~"    # 如果有写好的html文件（可以随便copy一个网站的源码），这里可以用文件打开的方式对其进行读取，然后发送过去

    response_content = header + body
    new_socket.send(response_content.encode("utf-8"))

    new_socket.close()

def main():
    # 创建套接字
    tcp_server_socket = socket(AF_INET, SOCK_STREAM)
    # 绑定
    local_addr = ("", 8888)
    tcp_server_socket.bind(local_addr)
    # 变为监听套接字
    tcp_server_socket.listen(128)

    while True:
        # 等待新客户端的连接
        new_sokcet, client_addr = tcp_server_socket.accept()
        # 为这个客户端服务
        service_client(new_sokcet, client_addr)
        # 因为是服务器，套接字不关闭
    tcp_server_socket.close()   #关闭监听套接字
if __name__ == "__main__":
    main()