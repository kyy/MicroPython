""" https://docs.micropython.org/en/latest/esp8266/quickref.html#dht-driver

    -- настройка REPL для удаленного подключения:
        import webrepl_setup

    -- запуск вручную:
        import webrepl
        webrepl.start()
"""
""" https://github.com/kost/webrepl-python 
    отправка скрипта в консоль REPL 
"""


import webrepl


repl = webrepl.Webrepl(
    host='192.168.1.142',
    port=8266,
    password='12345')

resp = repl.sendcmd("import os; os.listdir()")
webrepl_cfg = repl.sendcmd('f = open("webrepl_cfg.py", "r");t = f.read();f.close();print(t)')

print(resp.decode("ascii"))
print(webrepl_cfg .decode("ascii"))

