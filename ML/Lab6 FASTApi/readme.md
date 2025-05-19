# Fast Api приложение
Написать FastApi приложение для оборачивания модели ввиде web сервиса. Полученый сервис упаковать в docker контейнер.

## Установка Docker

Необходим сервер на linux. Согласно гайду https://docs.docker.com/engine/install/debian/ устанавливаем docker
1. ``sudo install -m 0755 -d /etc/apt/keyrings``
2. ``sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc``
3. ``sudo chmod a+r /etc/apt/keyrings/docker.asc``
4. ``echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null``
5. Обновляем индексы ``sudo apt-get update``
6. Скачиваем нужный образ ``sudo docker pull python:3.9-slim``

## Установка FastAPI и настройка окружения

1. Создаём в директории пользователя сервер ``mkdir FastApi.server``
2. Создаём окружение ``python3 -m venv FastApi.server/fast_env``
3.  Активируем окружение ``. FastApi.server/fast_env/bin/activate ``
4. Устанавливаем FastAPI ``pip3 install 'fastapi[standart]'``
5. Устанавливаем uvicorn ``pip3 install 'uvicorn[standart]'``

## Создаём приложение

1. Создаём FastAPI приложение, файлы которого лежат в Git.
2. Пишем Dockerfile, который также находится в репозитории.

## Пакуем на сервер и запускаем
1.Упакованное приложение вместе с Dockerfile отправляем на сервер при помощи scp
	``scp -P port_num -r /LocalDir user@ip_address:/home/user/FastApi.server ``
2.Собираем образ 
	``sudo docker build -t ml .``
3.Создаём правило доступа через брандмауэр
	``sudo ufw allow 8888/tcp``
4.Запускаем контейнер
		``sudo docker run -dp ip_address:8888:3000 ml``
