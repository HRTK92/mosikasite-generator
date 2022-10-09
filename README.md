# mosikasite-generator

Google検索にたまに現れる、「もしかして: 」を再現できるサイトです。
検索結果には、検索したキーワードに関連するサイトのタイトルとURLがそのまま表示されます。
![](./images/example.png)

## インストール

リポジトリをクローンして、必要なものをインストールします。

```bash
git clone 
cd mosikasite-generator
pip install -r requirements.txt
```

## 使用方法

flaskを使う方法と、コマンドラインで実行する方法があります。

### コマンドライン

サイトを生成するには、`python3 mosikasite.py`を実行します。これにより、`output`ディレクトリにサイトが生成されます。

### フラスクアプリ

flaskアプリを実行するには、`python3 app.py`を実行します。すると、ポート`5000`でflaskサーバーが起動します。
