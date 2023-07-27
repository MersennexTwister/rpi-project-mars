# [Проект МАРС](http://176.120.8.20). Код аппаратной части

Программа Raspberry Pi 3 для [проекта МАРС](http://176.120.8.20)

### Содержание:
 - **rpi\_handler.py** - основной исполняемый файл
 - **rpi_image_cache** - папка для сохранения распознаваемых изображений
 - **conf.ini** - конфигурационный файл

 ### Использование:

 1. #### Клонируйте репозиторий
    
        $ git clone https://github.com/MersennexTwister/rpi-project-mars

 2. #### Заполните конфигурационный файл conf.ini в формате:

        [user-data]
        login='_ваш логин_'
        password = '_ваш пароль_'

        [system-data]
        root='/путь/до/репозитория/rpi-project-mars'
        url='http://176.120.8.20/'

    Важно, чтобы в конце root не было слеша.

 3. #### Запустите rpi_handler.py

        $ python3 rpi_handler.py 