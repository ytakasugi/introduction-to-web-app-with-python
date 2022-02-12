import socket

class TCPServer:
    # TCP通信を行うサーバを表すクラス
    def serve(self):
        print("=== サーバを起動します ===")

        try:
            # ソケットを生成
            server_socket = socket.socket()
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            # socketをlocalhostのポート8080番に割り当てる
            server_socket.bind(("172.17.169.200", 8080))
            server_socket.listen(10)

            # 外部からの接続を待ち、接続があったらコネクションを確率する
            print("=== クライアントからの接続を待ちます ===")
            (client_socket, address) = server_socket.accept()
            print(f"=== クライアントとの接続が完了しました remote_address: {address} ===")

            # クライアントから送られてきたデータを取得する
            request = client_socket.recv(4096)

            # クライアントから送られてきたデータをファイルに書き出す
            with open("server_recv.txt", "wb") as f:
                f.write(request)

            client_socket.close()

        finally:
            print("=== サーバーを停止します。 ===")

if __name__ == '__main__':
    server = TCPServer()
    server.serve()