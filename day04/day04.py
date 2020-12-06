#!/usr/bin/env python3
import re


def passportify(data):
    ls = []
    acc = ''
    for ln in data:
        if ln == '':
            ls.append(acc[:-1])
            acc = ''
        else:
            acc += ln + ' '
    return ls


def p1(data):
    pat = r'(\w+):(.*)'
    res = 0
    req = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    for passport in data:
        d = {k:v for (k,v) in [re.findall(pat, x)[0] for x in passport.split()]}
        if req <= set(d.keys()):
            res += 1
    return res


def is_year(yr, s, e):
    return yr.isnumeric() and s <= int(yr) <= e


def is_height(hgt):
    if hgt[-2:] == 'in':
        return 59 <= int(hgt[:-2]) <= 76
    elif hgt[-2:] == 'cm':
        return 150 <= int(hgt[:-2]) <= 193
    return False


def is_hair_color(hcl):
    return re.match(r'#[0-9a-f]{6}', hcl)


def is_eye_color(ecl):
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def is_passport_id(pid):
    return pid.isnumeric() and len(pid) == 9


def is_valid(byr, iyr, eyr, hgt, hcl, ecl, pid, cid=None):
    return is_year(byr, 1920, 2002) and is_year(iyr, 2010, 2020) and is_year(eyr, 2020, 2030) \
        and is_height(hgt) and is_hair_color(hcl) and is_eye_color(ecl) and is_passport_id(pid)


def p2(data):
    pat = r'(\w+):(.*)'
    res = 0
    req = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    for passport in data:
        d = {k:v for (k,v) in [re.findall(pat, x)[0] for x in passport.split()]}
        if req <= set(d.keys()) and is_valid(**d):
            res += 1
    return res


input = open('input.txt').readlines()
data = [line.rstrip() for line in input]
data = passportify(data)
print(f'part 1: {p1(data)}')
print(f'part 2: {p2(data)}')
