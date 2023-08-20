from libs.yyax import c, d, r, f, adress, DDOS
import os
import time
import random
import requests

hashtag = rf"{c.cyan('[')}{c.yellow('#')}{c.cyan(']')}"
exitText = rf"{c.cyan('[')}{c.yellow('0')}{c.cyan(']')} {c.cyan('Exit')}"

def screen():
    def clear_screen():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    clear_screen()

def options():
    opt = f"""
    
    {c.cyan('[')}{c.yellow('1')}{c.cyan(']')} {c.cyan('DoS Attack')}
    {c.cyan('[')}{c.yellow('2')}{c.cyan(']')} {c.cyan('UserRecon')}
    {c.cyan('[')}{c.yellow('3')}{c.cyan(']')} {c.cyan('Found Dirs')}
    {c.cyan('[')}{c.yellow('4')}{c.cyan(']')} {c.cyan('Adress by IP')}
    {c.cyan('[')}{c.yellow('Y')}{c.cyan(']')} {c.cyan('Yyax - Info')}
    {c.cyan('[')}{c.yellow('X')}{c.cyan(']')} {c.cyan('Exit')}
    
    {c.cyan('[')}{c.yellow('#')}{c.cyan(']')} {c.cyan('Choose an Option: ')}"""

    opt_choose = input(opt)

    if opt_choose == "1":

        opt2_choose2 = input(rf"""
    {c.cyan('[')}{c.yellow('1')}{c.cyan(']')} {c.cyan('Wi-Fi Attack')}
    {c.cyan('[')}{c.yellow('2')}{c.cyan(']')} {c.cyan('Site DoS')}

    {c.cyan('[')}{c.yellow('#')}{c.cyan(']')} {c.cyan('Choose an Option: ')}""")
        
        if opt2_choose2 == '1':

            target_ip = input(f"    {hashtag} {c.cyan('Target IP: ')}")
            target_port = int(input(f"    {hashtag} {c.cyan('Target Port: ')}"))
            packet_size = int(input(f"    {hashtag} {c.cyan('Packet size: ')}")) * 1000 * 1000

            d.attack(packet_size)

        elif opt2_choose2 == '2':

            slowloris_target_ip = input(f"    {hashtag} {c.cyan('Target IP: ')}")
            slowloris_target_port = input(f"    {hashtag} {c.cyan('Target PORT: ')}")
            
            threads4ddos = int(input(f"    {hashtag} {c.cyan('Threads Number (start in 10): ')}"))
            DDOS.start(target_ip=slowloris_target_ip, target_port=slowloris_target_port, num_threads=threads4ddos, packet_size_mb=2)

    elif opt_choose == "2":

        user4recon = input(f"    {hashtag} {c.cyan('Username: ')}")
        print('')
        r.recon(username=user4recon)

    elif opt_choose == "3":

        url = input(f"    {hashtag} {c.cyan('Target WebSite (with http/https): ')}")
        wordlist = 'libs/common.txt'
        f.dir(url=url, wordlist=wordlist)
    
    elif opt_choose == '4':

        ipt = input(rf"    {hashtag} {c.cyan('Target IP: ')}")
        ukey = input(rf"    {hashtag} {c.cyan('IPStack Key: ')}")
        
        url = f"http://api.ipstack.com/{ipt}?access_key={ukey}"
        response = requests.get(url)
        dados = response.json()
        latitude = dados['latitude']
        longitude = dados['longitude']
        coordenadas = f"{latitude}, {longitude}"
        tadress = adress.obter_endereco(lat=latitude, long=longitude)
        mapslink = rf"https://www.google.com/maps?q={latitude},{longitude}"
        print(rf"""
    {c.cyan('Adress by')} {c.yellow(ipt)}:
    {c.green(tadress)}
    {c.cyan('Coords by')} {c.yellow(ipt)}:
    {c.green(coordenadas)}
    {c.cyan('Google Maps Link by')} {c.yellow(ipt)}:
    {c.green(mapslink)}
""")
    
    elif opt_choose in ['y', 'Y']:
        yyax_info = rf"""
    {c.purple('Area of ​​expertise: Information security, development of tools aimed at red team and front-end developer')}
    {c.purple('Favorite programming languages, markup and any other names: python, php, html, css')}
    {c.purple('Github: https://github.com/Yyax13')}
    {c.purple('Discord: solo.yyax')}
    {c.purple('Pix: +55 (43) 99122-5928')}
    {c.purple('MetaMask Wallet: 0xA3Aa0aD78279819632439f21bFdbC375574b84bF')}"""
        print(yyax_info)

    elif opt_choose in ['x', 'X']:
        os.system('exit')
        pass
        

def banner():
    banner = f"""                                                                                                
      {c.blue('_/_/_/                                            _/      _/      _/              _/')}      
   {c.blue('_/        _/_/_/      _/_/_/    _/_/_/  _/  _/_/  _/_/_/_/  _/_/    _/    _/_/    _/_/_/_/')}   
    {c.green('_/_/    _/    _/  _/    _/  _/    _/  _/_/        _/      _/  _/  _/  _/_/_/_/    _/')}        
       {c.green('_/  _/    _/  _/    _/  _/    _/  _/          _/      _/    _/_/  _/          _/')}         
{c.yellow('_/_/_/    _/_/_/      _/_/_/    _/_/_/  _/            _/_/  _/      _/    _/_/_/      _/_/')}      
         {c.yellow('_/')}                                                                                     
        {c.yellow('_/')}                                                                                      
{c.cyan('Welcome to SpaartNet')}"""
    print(banner)

screen()
banner()
options()
