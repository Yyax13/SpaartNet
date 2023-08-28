#importando libs (passa no meu github, https://github.com/Yyax13)
#mereco nota extra so pelo brute force caesar
import time
from yyax import *
import os

hashtag = fr"{c.cyan('[')}{c.yellow('#')}{c.cyan(']')}"
num1 = fr"{c.cyan('[')}{c.yellow('1')}{c.cyan(']')}"
num2 = fr"{c.cyan('[')}{c.yellow('2')}{c.cyan(']')}"
num3 = fr"{c.cyan('[')}{c.yellow('3')}{c.cyan(']')}"
num4 = fr"{c.cyan('[')}{c.yellow('4')}{c.cyan(']')}"
num5 = fr"{c.cyan('[')}{c.yellow('5')}{c.cyan(']')}"
num6 = fr"{c.cyan('[')}{c.yellow('6')}{c.cyan(']')}"
num7 = fr"{c.cyan('[')}{c.yellow('7')}{c.cyan(']')}"
num8 = fr"{c.cyan('[')}{c.yellow('8')}{c.cyan(']')}"
num9 = fr"{c.cyan('[')}{c.yellow('9')}{c.cyan(']')}"
num10 = fr"{c.cyan('[')}{c.yellow('10')}{c.cyan(']')}"


def crypt(text, shift): 
    encrypted_text = "" 
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text #retorna o texto

def decrypt(encrypted_text, shift):
    return crypt(encrypted_text, -shift)

def decrypt_all_possible(text, max_shift=25):
    results = []
    
    for shift in range(max_shift + 1):
        decrypted_text = decrypt(text, shift)
        results.append(decrypted_text)
    
    return results

def format_output(decrypted_list):
    output = ""
    number = 1
    for decrypted in decrypted_list:
        print(f"""{c.yellow('|')} #{number} {c.green(decrypted)} {c.yellow('|')}\n""")
        number += 1
        time.sleep(1.111)

def main():
    opt = input(rf"""
    {num1} {c.cyan('Caesar encrypt')}
    {num2} {c.cyan('Caesar decrypt')}
    
    {hashtag} {c.cyan('Choose an option: ')}""")
   
    if opt == "1":
      text4crypt = input(rf"    {hashtag} {c.cyan('Text to encrypt: ')}")
      caesar_key = int(input(f"    {hashtag} {c.cyan('Encrypter key: ')}"))
      final_crypted_text = crypt(text=text4crypt, shift=caesar_key)
      print(rf""" 
    {c.cyan('Final text crypted on the key')} {c.yellow(caesar_key)}:
    {final_crypted_text}""")
    elif opt == "2":
       opt_d = input(rf""" 
    {num1} {c.cyan('Enter Key')}
    {num2} {c.cyan('Brute Force')}

    {hashtag} {c.cyan('Choose an option: ')}""" )
       if opt_d == "1":
          text4decrypt = input(f"    {hashtag} {c.cyan('Cripted text: ')}")
          caesar_dkey = int(input(f"    {hashtag} {c.cyan('Decrypter key: ')}"))
          final_dcrypted_text = decrypt(encrypted_text=text4decrypt, shift=caesar_dkey)
       elif opt_d == "2":
          text4decrypt = input(f"    {hashtag} {c.cyan('Cripted text: ')}")
          final_dcrypted_text = decrypt_all_possible(text=text4decrypt)
          finalD_format = format_output(final_dcrypted_text)
          print("\n")
          print(finalD_format)     

    input(f"{c.red('Press enter to quit')}")

if __name__ == "__main__":
   main()
