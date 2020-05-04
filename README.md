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
После чего сайт будет доступен по адресу: http://127.0.0.1:5000/ 

5. На работу я заложил 4 дня, с 30.04.2020 по 04.05.2020
6. Реально потратил дня 3 с небольшим.

Что не получилось реализовать:

- Не получилось запустить nginx в докере, при попытке его запустить докер выкидывал ошибку:
```shell script
ERROR: for simbir-soft_web_1  UnixHTTPConnectionPool(host='localhost', port=None): Read timed out. (read timeout=120)

ERROR: for web  UnixHTTPConnectionPool(host='localhost', port=None): Read timed out. (read timeout=120)
ERROR: An HTTP request took too long to complete. Retry with --verbose to obtain debug information.
If you encounter this issue regularly because of slow network conditions, consider setting COMPOSE_HTTP_TIMEOUT to a higher value (current value: 120).

```
после чего сам умерал, помогает только выход из докера, с последуюцим запуском приложения докер, простой рестарт докера, то же не помогает. Возможно это проблема только у меня.

В лубом случает в docker-compose файле есть конфиг для nginx - а, при желании, можно раскомментировать его и попробовать запустить, если запуск пройдет успешо, тогда flask будет проксироваться nginx - ом на порт **8000**  и сайт будет доступен по адресу: http://127.0.0.1:8000/
