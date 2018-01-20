#!/bin/env python
# -*- coding:utf-8 -*-

import os

import MeCab

nm = MeCab.Tagger("-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
labeled = []

def main():
    """
    データの取得、ラベル付けと分かち書き
    """
    data_list = os.listdir('./../ml_data')
    for data in data_list:
        if data == 'target.txt':
            label = '__label__1, '
        elif data == 'other.txt':
            label = '__label__2, '
        else:
            print(data,'pass')
            continue
        with open('./../ml_data/'+data) as f:
            lines = f.readlines()
        for l in lines:
            labeled.append(refactor(label, l))
    with open('./../ml_data/label_negaposi.lst', 'w') as f:
        f.write('\n'.join(labeled))

def refactor(label, text):
    """
    分かち書きしてラベルを付して返す
    """
    # 自分のTL,井口さんのTLに頻繁に現れるものの、本人の文章の特徴としてそぐわない
    # 単語をストップワードとして除去しています。
    bl = ['慶応', '慶應', 'SFC', 'sfc', 'ミス', 'ミスター', '青学', 'ミスコン']
    wakatied = nm.parse(text)
    wakatied = [word for word in wakatied.split(' ') if word not in bl]
    return label + ' '.join(wakatied)

if __name__ == '__main__':
    main()
