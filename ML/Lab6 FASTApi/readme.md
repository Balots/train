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
