# flaskをdocker環境で構築するテンプレート

### 環境構築
```
$ docker-compose build
```

### 起動
```
$ docker-compose up -d
$ docker-compose exec flask bash
$ flask run --host 0.0.0.0 --port 5000
```

### IDE(PyCharm)環境構築
```
Preference>Project:プロジェクト名>Project Interpreter>歯車>add>Docker..からイメージを選択
Project InterpreterにRemote Python ３.◯.◯ Dockerを選択
Run/Debug Configratonのtargetをモジュール選択に切り替えsrc.appにする
```

### GAEにデプロイ
```
/src に入って
$ gclpud init
$ gcloud app deploy
```
