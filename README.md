# Sudden Death

＿人人人人人人＿  
＞　突然の死　＜  
￣Y^Y^Y^Y^Y￣

↑を簡単に作るためのPythonスクリプトです。

## Requirements

- Python 3.5 over
- ```pip install -r requirements.txt```

## Usage

sd.pyを実行することで次に入力した文字が吹き出しになって出力されます。  
-c, --copy オプションをつけることでで結果をクリップボードにコピー  
-q, --quiet オプションをつけることで結果を出力しません

```
$ python sd.py Hello World
＿人人人人人人人人＿
＞　Hello World!　＜
￣Y^Y^Y^Y^Y^Y^Y^Y￣
$ python sd.py -c
Please input some sentence:突然の死!
＿人人人人人人＿
＞　突然の死!　＜
￣Y^Y^Y^Y^Y^Y￣ # クリップボードにコピー
$ python sd.py -cq 突然の死! # クリップボードにコピーし、出力はしない
```

## License

[MIT LICENSE](LICENSE)

## Author

- [koluku](https://github.com/koluku)