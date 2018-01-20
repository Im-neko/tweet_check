# tweet_cheker
ツイートがどれくらい似ているかを判定するモデルです
一緒に入っている分類モデルはミス青学準グランプリの井口綾子さんのツイートで
作成したモデルです。
ネタです。

### 環境
- MacBook HighSierra
- python3
    - fasttext
- mecab neologd

### 環境構築
mecab、neologdの構築は飛ばします。
https://qiita.com/nkjm/items/913584c00af199794257
こちらの記事など丁寧に記述されていてわかりやすいです。
mecab+neologdが終わった後は、
`git clone git@github.com:Im-neko/tweet_check.git`
`cd ayako_chek`
`pip3 install -r piplist.txt`
でOKです。
 
### 使い方
- すでに学習済みモデル(井口綾子さん)を使う場合
    - 環境構築が終わっていれば、`python3 predict.py ドイツの科学力は世界一ィィイイイイ`
    - みたいに入力すると判定してくれます
- 特定の誰かのツイートを学習させたい場合
    - keys.jsonに自分のAPIkeyを書く
    - gettweet.pyを自分の使いたいように編集する。
        - デフォルトでは井口綾子さんになってます
    - `python3 gettweet.py`
    - `python3 data_refactor.py`
    - `pyhton3 makemodel.py`
    - ここまで実行すると判定用のモデルがsrcフォルダの中に生成されます。
- 後は`python3 predict.py ドイツの科学力は世界一ィィイイイイ`みたいな感じで実行すると判定してくれます

### その他
本来著者推定などは句読点などを重視して行う必要があるのに対して、
今回使用したfasttextでは単語の共起頻度、つまりは「どんな単語が一緒に現れやすいか」という部分を使用して判定しています。
なので、厳密には「井口綾子さんの言葉遣いにどれだけ似ているかを判定する分類器」
というのが正しいかもしれません。
ですので、実際に井口綾子さんが書いた文章に近いかどうかというのは分かりません。
ただ、井口綾子さんが@ayako_17miss4で発信指定た内容に近い言葉遣いのかどうかというものに関してはある程度判定してくれるかと思います。


雑に書いてしまったので何かあればTwitter:@Im_nukoまで連絡ください。

