#!/bin/bash
echo "📦 Установка Git Hooks в директорию .git/hooks..."
if [ -d ".githooks" ]; then
    cp .githooks/* .git/hooks/
    chmod +x .git/hooks/*
    echo "✅ Все хуки успешно установлены и активированы."
else
    echo "❌ Директория .githooks не найдена."
    exit 1
fi