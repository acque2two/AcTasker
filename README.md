# AcTasker
Original Task management tool on Web 


# 現状
## 動作環境
* Python + MongoDB
    * RDBよりドキュメント志向DBの方が実装が容易でストレージの無駄が少ないと考えた
        * RDBほどの堅牢性が不要で検索機能もSQLが必要なほどではない
    * MongoDBを触ってみたかった
    * 本来のRust実装だと時間が足りない
* HTML + ごくわずかなJavaScript + BootStrap ( w/ Pingendo )
    * コストを最小限に抑えたかった

## 使用ライブラリ
* Flask
    * Web通信のため・付属テンプレートエンジン(Jinja2)を使用, REST用にFlask-RESTfulも使用予定
    * Djangoより軽く、 Bottleよりセッションの扱いが楽・フレームワークを拡張するライブラリが充実
* MongoEngine
    * MongoDBの操作に使用
    * PyMongoより柔軟性が低く、固定されたスキーマを扱うのに有利？・IDEでの補完が出やすい



# 展望
* React化
    * RESTをReactフロントで叩くのが理想
* 処理をもっとフロントエンドに任せたい
    * バックエンドでの処理量を減らしてコスト削減と処理の高速化をしたい
* Rustでバックエンドを再実装
    * もともと中途半端なRust実装をPython実装に落とし込み直してる
        * 実装は簡単だが低速

# 希望
* FireBaseをバックエンドにできるようにしたい
    * React NativeでAndroidアプリ化・通知の有効化
    * Realtime Databaseでバックグラウンド処理の最適化
    * Firebase Functionで処理の煩雑さの低減
    * もはやサーバプログラムが不要に！