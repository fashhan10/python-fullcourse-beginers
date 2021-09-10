#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 22:35:14 2021

@author: bocuin
@source: https://www.inpows.com/python/menampilkan-informasi-cpu-menggunakan-psutil-di-python/
"""

import psutil


def cpu_info():
    print("*"*10,"CPU Information","*"*10)
    print("Physical Cores: ", psutil.cpu_count(logical=False))
    print("Total Cores: ", psutil.cpu_count(logical=True))

    cpu_freq = psutil.cpu_freq()
    print(f"Max Frequency: {cpu_freq.max:.2f}Mhz")
    print(f"Min Frequency: {cpu_freq.min:.2f}Mhz")
    print(f"Current Frequency: {cpu_freq.current:.2f}Mhz")

    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True,interval=1)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")


if __name__ == "__main__":
    cpu_info()