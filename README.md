# [Проект МАРС](http://45.12.18.75). Код аппаратной части

Программа Raspberry Pi 3 для [проекта МАРС](http://45.12.18.75)

### Содержание:
 - **rpi\_handler.py** - основной исполняемый файл
 - **rpi_image_cache** - папка для сохранения распознаваемых изображений
 - **conf.ini** - конфигурационный файл
 - **mainloop.py** - скрипт, запускающийся при прерывании программы и отображающий лог
 - **log** - лог распознаваний
 - **auto.sh** - скрипт автозапуска

 ### Использование:

 1. #### Клонируйте репозиторий
    
        $ git clone https://github.com/MersennexTwister/rpi-project-mars

 2. #### Заполните конфигурационный файл conf.ini в формате:

        [user-data]
        login=_ваш логин_
        password = _ваш пароль_

        [system-data]
        root=/путь/до/репозитория/rpi-project-mars
        url=http://176.120.8.20/

    Важно, чтобы в конце root не было слеша.

 3. #### Исправьте пути до conf.ini и rpi_handler.py в auto.sh

 4. #### Запустите auto.sh

        $ ./auto.sh


### Бонус. Автозапуск

Если необходимо, чтобы скрипт запускался при запуске системы, откройте файл:

       $ sudo vi /etc/xdg/lxsession/LXDE-pi/autostart

И напишите в предпоследнюю строку файла:

       @lxpanel --profile LXDE-pi
       @pcmanfm --desktop --profile LXDE-pi

       @lxterminal -e "/path/to/auto.sh" //<- надо вставить это

       @xscreensaver -no-splash
