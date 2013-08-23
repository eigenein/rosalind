#!/usr/bin/env python3
# -*- coding: utf-8 -*-

k, m, n = map(int, input().split())
S = k + m + n
s = S - 1

p = sum((
    (k / S) * ((k - 1) / s) * 1.0,  # YY vs YY
    (k / S) * (m / s) * 1.0 * 2,  # YY vs Yy and Yy vs YY
    (k / S) * (n / s) * 1.0 * 2,  # YY vs yy and yy vs YY
    (m / S) * ((m - 1) / s) * 0.75,  # Yy vs Yy
    (m / S) * (n / s) * 0.5 * 2,  ## Yy vs yy and yy vs Yy
))

print(p)
