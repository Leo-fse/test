## PythonのBokehライブラリを用いたグラフ化ツール

このプロジェクトは、エクセルの設定データに基づいてグラフを作成し、出力するためのツールです。

## 使用方法
1. `data/input/setting.xlsm`を編集します。
2. 以下のコマンドを実行します：
   ```bash
   python src/main.py
   ```
3. 結果がdata/output/フォルダに保存されます。

## 環境構築
1. 必要なライブラリをインストールします。
    ```
    pip install -r requirements.txt
    ```


## フォルダ構成
フォルダ構成は以下の通りです。　
```
Project/
├── src/
│   ├── __init__.py
│   ├── __main__.py
│   ├── settings.py
│   ├── libs/
│   │   ├── __init__.py
│   │   └── read_setting.py
│   │   └── drawing_graph.py
│   │
│   ├── utils/
│   │    ├── __init__.py
│   │    └── database.py
│   │
├── config/
│   ├── database.ini
│   │
│   ├── input/
│   │   ├── setting.xlsm
│   ├── output/
│   │   ├── data.xlsx
│   │   ├── graph.html
│   │
├── tests/
│
├── README.md
├── .venv/
├── .vscode/
└── requirements.txt
```
