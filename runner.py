#!/usr/local/bin/python env
# coding:utf-8

import pytest


def test_001():
    print("abc")


if __name__ == '__main__':
    pytest.main("-q demo1.py")
