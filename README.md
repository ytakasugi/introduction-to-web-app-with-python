# [伸び悩んでいる3年目Webエンジニアのための、Python Webアプリケーション自作入門](https://zenn.dev/bigen1925/books/introduction-to-web-application-with-python/viewer/preface)

## python

- [Python関連記事まとめ](https://note.nkmk.me/python-post-summary/)

## 文法メモ

### with文

#### 用途

「開始」と「終了」がセットになった処理に使う。

- ファイルを開いて読み書きを行う。
- DBにアクセスし処理後に終了するなど。

#### 処理内容

「開始」と「終了」がセットになる処理で、with文を使って「開始」すると、処理実行後に自動で「終了」してくれる。

#### メリット

- 終了の処理を書かなくていい。
- 終了の処理を書き忘れることがない。

#### 基本構文

```python
with 開始処理 as 変数
    処理
```

- 開始処理

ファイルを開くなどの、通信を開始する処理を記述。

- 変数

処理①を呼び出すための変数（略称）

- 処理

実行する処理。この処理が完了すると自動で後始末を実行する

---

### [例外処理](https://note.nkmk.me/python-try-except-else-finally/)

### 関数、クラスメソッド

- [Pythonで関数を定義・呼び出し（def, return）](https://note.nkmk.me/python-function-def-return/)
- [クラスメソッドの引数にselfを使う理由](https://codor.co.jp/python/reason-to-use-self)