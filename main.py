from statistics import mean
import time
from web3 import Web3
import requests
import random
from datetime import datetime
import config
import fun
from fun import *



current_datetime = datetime.now()
print(f"\n\n {current_datetime}")
print(f'============================================= Плюшкин Блог =============================================')
print(f'subscribe to : https://t.me/plushkin_blog \n============================================================================================================\n')

clear_csv_file("no_money")
clear_csv_file("result")
keys_list = []
with open("private_keys.txt", "r") as f:
    for row in f:
        private_key=row.strip()
        if private_key:
            keys_list.append(private_key)

i=0
for private_key in keys_list:
    i+=1
    if config.proxy_use == 2:
        while True:
            try:
                requests.get(url=config.proxy_changeIPlink)
                fun.timeOut("teh")
                result = requests.get(url="https://yadreno.com/checkip/", proxies=config.proxies)
                print(f'Ваш новый IP-адрес: {result.text}')
                break
            except Exception as error:
                print(' !!! Не смог подключиться через Proxy, повторяем через 2 минуты... ! Чтобы остановить программу нажмите CTRL+C или закройте терминал')
                time.sleep(120)

    try:
        web3 = Web3(Web3.HTTPProvider(config.conf['rpc'], request_kwargs=config.request_kwargs))
        account = web3.eth.account.from_key(private_key)
        wallet = account.address    
        log(f"I-{i}: Начинаю работу с {wallet}")
        balance = web3.eth.get_balance(wallet)
        balance_decimal = Web3.from_wei(balance, 'ether')
        balance_decimal_USD = balance_decimal * config.conf['price']
        log(f"balance = {balance_decimal}")
        count=web3.eth.get_transaction_count(wallet)


        if balance_decimal <= config.minimal_need_balance:
            save_to_csv_file("no_money",[private_key,wallet,balance_decimal])
        else:
            save_to_csv_file("result",[private_key,wallet,balance_decimal,balance_decimal_USD,count])


    except Exception as error:
        fun.log_error(f'ERROR: {error}')    
        keys_list.append(private_key)
        timeOut("teh")
        continue


        
  
    
log("Ну типа все, кошельки закончились!")        

