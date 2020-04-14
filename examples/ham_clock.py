#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2014-18 Richard Hull and contributors
# Copyright (c) 2020 Michael Bergeron <mikeb.code@gmail.com>
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

"""
An analog clockface with date & time.

MBergeron: Copied from clock.py in this directory.

Ported from:
https://gist.github.com/TheRayTracer/dd12c498e3ecb9b8b47f#file-clock-py
"""

from datetime import datetime
from demo_opts import get_device
from luma.core.render import canvas
import math
import PIL
import time


def main():
    last_time = None
    cy = min(device.height, 64) / 2
    cx = min(device.width, 128) / 2

    while True:
        now = datetime.now()
        if now != last_time:
            with canvas(device) as draw:
                now = datetime.now()
                utc_now = datetime.utcnow()
                local_time = now.strftime("%H:%M:%S")
                local_date = now.strftime("%d %b %y")

                utc_time =utc_now.strftime("%H:%M:%S")
                utc_date = utc_now.strftime("%d %b %y")


                # Local
                draw.text((2, 2), local_time, fill="yellow")
                draw.text((2, 10), local_date, fill="yellow")

                # UTC
                draw.text((2, cy), "== UTC ==", fill="yellow")
                draw.text((2, cy+8), utc_time, fill="yellow")
                draw.text((2, cy+16), utc_date, fill="yellow")

        time.sleep(0.1)


if __name__ == "__main__":
    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass
