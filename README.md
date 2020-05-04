1. Марьев Евгений Дмитриевич. **Email**: kadr1986@gmail.com
2.  Структура проекта:
        
        - app - папка с проектом
            - blog - blueprint для постов, это те которые храняться в редиске. Функционал: добавить, достать
            - migrations
            - models
                - user - класс для работы с пользователями
            - static
            - templates - общие шаблоны, базовый layout
            - user - blueprint для регистрации и авторизации
            - app.py - файл инициализатор flask - а
            - config.py - класс с конфигурацими flask - а
            - requirements.txt - зависимости
            - runer.py - менеджер
            - view.py - контроллер для главной  
        - nginx - конфиг для nginx - а
        - redis-data - конфиг для редиса
        - .env - конфигурации для докера
        - .gitignore
        - docker-compose.yml
        - Dockerfile
3. В проете использовал такие библиотеки:
        
        - Flask-Login - для организации авторизации пользователей
        - Flask-Migrate - для организации миграций 
        - Flask-Script - для создания консольных команд
        - Flask-SQLAlchemy - орм для Postresql - а
4. Для запуска, нужно в папке с проектом выполнить команду:
```shell script
docker-compose up --build
или
docker-compose up -d --build - что бы запустить в режиме демона
```
после того, как проект соберется и запуститься, нужно прогнать миграцию:
```shell script
docker-compose exec flask python runner.py db upgrade
```
После чего сайт будет досиупен по адресу: http://127.0.0.1:5000/ 

5. На работу я заложил 4 дня, с 30.04.2020 по 04.05.2020
6. Реально потратил дня 3 с небольшим.
