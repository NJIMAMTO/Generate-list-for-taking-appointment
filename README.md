# 電話アポをとるためのリスト生成

## Description
電話でアポイントや営業をかけたいときに一件一件検索せずにまとめて検索できれば便利ですよね？

そんなときにこれを使えば地域とキーワードを指定すれば該当する店舗や電話番号をリスト形式で表示してくれます

## Demo
入力画面の一例

<img src="https://user-images.githubusercontent.com/41196217/75736198-e7b5de00-5d3f-11ea-9ca0-f4637a5d5588.png" width="480px">

出力画面の一例

<img src="https://user-images.githubusercontent.com/41196217/75736263-12079b80-5d40-11ea-88f6-5f67553e0556.png" width="480px">

## Usage
ターミナル上で次のコマンドを実行してください
```
python main.py
```
## Install
インストール方法は以下の通りです
```
git clone <this repository name>

pip install PySimpleGUI==4.16.0
pip install pandas==0.25.1
pip isntall selenium==3.141.0
```

別途ダウンロードしたchromedriverをpythonのパッケージフォルダに入れておく必要があります。

ダウンロード先↓

https://chromedriver.chromium.org/downloads
