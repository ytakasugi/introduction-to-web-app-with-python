from webserver import WebServer

if __name__ == "__main__":
    # Webserverクラスのインスタンスを生成する
    server = WebServer()
    # serveメソッドを呼び出す
    server.serve()