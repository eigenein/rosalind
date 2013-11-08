#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n, k = map(int, input().split())

fib = {1: 1, 2: 1}
for i in range(3, n + 1):
    fib[i] = fib[i - 2] * k + fib[i - 1]

print(fib[n])
