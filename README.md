# Автор
PLushkin https://t.me/plushkin_blog        

**На чай с плюшками автору:**
Полигон, БСК, Арбитрум - любые токены - `0x79a266c66cf9e71Af1108728e455E0B1D311e95E`

Трон TRC-20 только USDT, остальное не доходит - `TEZG4iSmr31wWnvBixKgUN9Aax4bbgu1s3`

# Чё делает
Простой чекер нативного баланса в ЕВМ сетях. так же покажет общее число транзакций на кошельке в этой сети.
Результат делит на две таблицы - пустые кошельки и кошельки с балансом



# Настройка
Укажите приватные ключи в файле private_keys
в низу файла config укажите
price цену нативного токена, для правильного пересчета
rpc той ЕВМ сети в которой вы хотите снять статистику

# Установка и запуск:

Linux/Mac - https://www.youtube.com/watch?v=8rJ-96cPFwU
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python main.py
```
Windows - https://www.youtube.com/watch?v=EqC42mnbByc
```
pip install virtualenv
virtualenv .venv
.venv\Scripts\activate
pip install -r requirements.txt

python main.py
```


