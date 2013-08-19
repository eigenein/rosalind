#!/usr/bin/env python3
# -*- coding: utf-8 -*-

complements = dict(zip("ATCG", "TAGC"))
print("".join(map(complements.get, input()), )[::-1])
