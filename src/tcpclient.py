import socket

class TCPClient:
    def request(self):
        print("=== クライアントを起動します ===")

        try:
            # ソケットを生成
            client_socket = socket.socket()
            client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            # サーバと接続
            print("=== サーバーと接続します ===")
            client_socket.connect(("172.17.168.86", 80))
            print("=== サーバーとの接続が完了しました ===")

            # サーバに送信するリクエストを、ファイルから取得する
            with open("client_send.txt", "rb") as f:
                request = f.read()

            # サーバへリクエストを送信する
            client_socket.send(request)

            # サーバーからレスポンスが送られてくるのを待ち、取得する
            response = client_socket.recv(4096)

            # レスポンス内容をファイルに書き出す
            with open("client_recv.txt", "wb") as f:
                f.write(response)

            client_socket.close

        finally:
            print("=== クライアントを停止します。 ===")

if __name__ == '__main__':
    client = TCPClient()
    client.request()