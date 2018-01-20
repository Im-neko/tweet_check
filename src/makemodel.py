#!/usr/bin/env python
# -*- coding:utf-8 -*-

import fasttext as ft

classifier = ft.supervised('./../ml_data/label_negaposi.lst', 'model')
