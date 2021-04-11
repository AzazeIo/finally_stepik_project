<H1>Учебные тесты для WEBа</H1>

**Описание:** В папке <i>finally_stepik_progect</i> представлены все задания за 4 модуль из курса https://stepik.org/course/575/syllabus.

<H2>Настройка окружения</H2>

**Установить Python 3+**
https://www.python.org/downloads/

**Установиить pip:**
https://pip.pypa.io/en/stable/installing/#installing-with-get-pip-py

**Установить pipenv:**
https://pypi.org/project/pipenv/

**Установить selenium для Python:**
<br><code>pip install selenium==3.14.0</code>

**Установить WebDriver:**
Для начала узнаем версию нашего браузера(Справка - О Браузере Google Chrome)
По ссылке https://sites.google.com/a/chromium.org/chromedriver/downloads скачиваем ту версию драйвера, которая совпадает с версией браузера. 
<br>По порядку выполняем следующие команды:
1) Открыть папку с загрузками:
   <br><code>cd ~/Downloads</code>
2) Открыть архив с драйвером: 
   <br><code>wget https://chromedriver.storage.googleapis.com/76.0.3809.68/chromedriver_mac64.zip </code>
3) Распоковать архив с драйвером:
   <br><code>unzip chromedriver_mac64.zip</code>
4) Переместить папку с драйвером в необходимую директорию:
   <br><code>sudo mv chromedriver /usr/local/bin</code>
5) Проверить версию драйвера:
   <br><code>chromedriver --version</code>
6) Если все ок, получаем ответ:
<br><code>ChromeDriver 76.0.3809.68 (420c9498db8ce8fcd190a954d51297672c1515d5-refs/branch-heads/3809@{#864})</code>

<H2>Настройка интерпретатора в PyCharm</H2>

Переходим в PyCharm - Preferences - Python Interpreter.
Кликаем по шестиренке в правом верхнем углу окна и выбираем "add".
В настройках выбираем Pipenv Environment, задаем путь до директории test и нажимаем ОК.
<br><b>ВАЖНО! Проверить, что в интерпритере есть необходимые пакеты для запуска тестов (В настройка интерпритера должны быть пакеты selenium и urllib3)</b>

<H2>Устновка пакетов из requirements.txt</H2>
<br><code>pip install -r /path/to/requirements.txt</code>
<br><code> pip install -r requirements.txt --no-index --find-links file:///tmp/packages</code>
