#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


s, t = input(), input()
print(" ".join(str(match.start() + 1) for match in re.compile("(?=%s)" % t).finditer(s)))
