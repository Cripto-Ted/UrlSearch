#!/bin/bash

# Обновляем список пакетов
echo "Обновление списка пакетов..."
sudo apt update

# Устанавливаем pip, если он не установлен
if ! command -v pip &> /dev/null
then
    echo "pip не найден. Устанавливаем pip..."
    sudo apt install python3-pip -y
fi

# Устанавливаем необходимые библиотеки
echo "Устанавливаем необходимые библиотеки..."
pip install requests beautifulsoup4

# Переходим в директорию с вашим скриптом
echo "Переход в директорию с вашим скриптом..."
cd путь/к/вашему/UrlSearch || { echo "Директория не найдена"; exit 1; }

# Запускаем ваш Python-скрипт
echo "Запускаем ваш скрипт..."
python3 UrlSearch.py
