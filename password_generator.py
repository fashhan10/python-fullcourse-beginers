#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 21:14:58 2021

@author: bocuin
@source: https://geekflare.com/password-generator-python-code/
"""
import random
import string 

##karakter untuk menghasilkan kata sandi dari
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
    ##pajang password dari pengguna
    length = int(input("masukkan digit password: "))
    
    ##mengacak karakter password
    random.shuffle(characters)
    
    ##mengambil karakter acak dari list ( listnya adalah string )
    password = []
    for i in range(length):
        password.append(random.choice(characters))
        
    #password acak yang dihasilkan
    random.shuffle(password)
    
    #mengubah list menjadi string
    #cetak list
    print("".join(password))
    
    
    
##menjalankan fungsi
generate_random_password()