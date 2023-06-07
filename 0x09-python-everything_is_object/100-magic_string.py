#!/usr/bin/python3
def magic_string():
    magic_string.cn = magic_string.cn + 1 if hasattr(magic_string, 'cn') else 1
    return ', '.join(['BestSchool'] * magic_string.cn)
