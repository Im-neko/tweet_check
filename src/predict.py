#/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import subprocess as cmd

import fasttext as ft
import MeCab

data = {'__label__1,': 'ayako', '__label__2,': 'other', '__label__3,': 'mori'}

def main(text):
    """
    MeCabで分かち書きした後に作成したモデルを読み込み、判定
    MeCabのneologdの保存されているpathはmacなら大抵ここになるはずではあるが、エラーが出た際は調べて修正してください。
    """
    nm = MeCab.Tagger("-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
    words = nm.parse(text).replace('\n', '   ')
    print(words)
    classifier = ft.load_model('./model.bin')
    estimate = classifier.predict([words], k=3)
    estimate_2 = classifier.predict_proba([words], k=3)
    if estimate[0][0] == '__label__2,':
        print('最も近いのは: other', estimate_2[0][0][1])
        print(data[estimate_2[0][0][0]], estimate_2[0][0][1], data[estimate_2[0][1][0]], estimate_2[0][1][1])
    elif estimate[0][0] == '__label__1,':
        print('最も近いのは: ayako', estimate_2[0][0][1])
        print(data[estimate_2[0][0][0]], estimate_2[0][0][1], data[estimate_2[0][1][0]], estimate_2[0][1][1])

if __name__ == '__main__':
    if sys.argv[1]:
        main(str(sys.argv[1]))
    else:
        print('引数に判定したいテキストを入力してください')
