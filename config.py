
#то что ниже обязательно заполнить своими данными
proxy_use = 0 #  0 - не использовать, 1 - прокси без ссылки , 2 - прокси со ссылкой для смены ip
proxy_login = 'pfd56464'
proxy_password = '9caa07'
proxy_address = 'noroxy.com'
proxy_port = '107'
proxy_changeIPlink = "httpcce3b204"


#то что ниже желательно настроить под себя
minimal_need_balance = 0 # минимальный баланс на кошельке который должен быть, все что ниже считаем 0
#задержки между операциями в рамках одного кошелька
timeoutTehMin = 3 #минимальная 
timeoutTehMax = 10 #максимальная


#то что ниже можно менять только если понимаешь что делаешь
proxies = { 'all': f'http://{proxy_login}:{proxy_password}@{proxy_address}:{proxy_port}',}
if proxy_use:
    request_kwargs = {"proxies":proxies, "timeout": 1200}
else:
    request_kwargs = {"timeout": 120}

slippage = 1    # % 
gas_kef=1.1 #коэфициент допустимого расхода газа на подписание транзакций. можно выставлять от 1.1 до 2

conf = {
    'price': 3000,
    'rpc': 'https://rpc.ankr.com/scroll',
}