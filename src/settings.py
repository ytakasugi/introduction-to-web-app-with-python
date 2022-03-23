from re import L
import os
import socket

# 実行ファイルのあるディレクトリ
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 静的配信するファイルを置くディレクトリ
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# テンプレートファイルを置くディレクトリ
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

# IPアドレスを取得
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP_ADDR = s.getsockname()[0]