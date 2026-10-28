# Системы контроля версий (VCS)

<p align="center">
  <img src="https://img.shields.io/badge/СКФУ-Институт_цифрового_развития-0055A5?style=for-the-badge&logo=google-scholar&logoColor=white" alt="NCFU"/>
  <img src="https://img.shields.io/badge/Специальность-09.03.03_Прикладная_информатика-blue?style=for-the-badge" alt="Specialty"/>
  <img src="https://img.shields.io/badge/Студент-Мухамеджанов_Эльёр_Тимурович-orange?style=for-the-badge" alt="Student"/>
  <img src="https://img.shields.io/badge/Группа-ПИН--б--о--24--1(2)-green?style=for-the-badge" alt="Group"/>
</p>

<p align="center">
  <a href="https://gitlab.com/TheLegendMaster/hello-git">
    <img src="https://img.shields.io/badge/GitLab_Mirror-TheLegendMaster%2Fhello--git-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white" alt="GitLab Mirror"/>
  </a>
  <img src="https://img.shields.io/badge/Статус_курса-Лабораторные_1--5_выполнены-success?style=for-the-badge" alt="Status"/>
</p>

---

## 📌 О репозитории

Данный репозиторий содержит лабораторные работы, отчёты и практические проекты по университетской дисциплине **«Системы контроля версий»** (3 курс, 5 семестр).

* **Учебное заведение:** Федеральное государственное автономное образовательное учреждение высшего образования «Северо-Кавказский федеральный университет» (СКФУ)
* **Институт:** Институт цифрового развития
* **Направление:** 09.03.03 «Прикладная информатика»
* **Студент:** Мухамеджанов Эльёр Тимурович
* **Группа:** ПИН-б-о-24-1(2)
* **Год:** 2026

---

## 📋 Навигатор по лабораторным работам

| № | Тема работы | Отчёт | Исходный код / Файлы | Статус |
|:---:|:---|:---:|:---:|:---:|
| **01** | Установка и настройка Git, создание SSH-ключа, работа с GitLab | [📄 Отчёт №1](Отчеты/Отчет_Лабораторная_1.md) | [📁 Файлы проекта](Лабораторные_работы/01_02_hello-git/) | ✅ **Сдано / Выполнено** |
| **02** | Ветвление, слияние и разрешение конфликтов в Git | [📄 Отчёт №2](Отчеты/Отчет_Лабораторная_2.md) | [📁 Файлы проекта](Лабораторные_работы/01_02_hello-git/) | ✅ **Сдано / Выполнено** |
| **03** | Работа с удалёнными репозиториями. Совместная разработка в GitLab | [📄 Отчёт №3](Отчеты/Отчет_Лабораторная_3.md) | [📁 Файлы проекта](Лабораторные_работы/03_collab-project/) | ✅ **Сдано / Выполнено** |
| **04** | Управление историей коммитов: rebase, reset, revert и интерактивный rebase | [📄 Отчёт №4](Отчеты/Отчет_Лабораторная_4.md) | [📁 Файлы проекта](Лабораторные_работы/04_history-management/) | ✅ **Сдано / Выполнено** |
| **05** | Автоматизация разработки: Git Hooks и GitLab CI/CD | [📄 Отчёт №5](Отчеты/Отчет_Лабораторная_5.md) | [📁 Файлы проекта](Лабораторные_работы/05_hooks-and-cicd/) | ✅ **Сдано / Выполнено** |
| **06** | GitLab CI/CD: Пайплайн автоматизации сборки, тестирования и развертывания | 📄 *В процессе* | 📁 *В процессе* | ⏳ Запланировано |
| **07** | Окружения, Review Apps и управление развертыванием в GitLab | 📄 *В процессе* | 📁 *В процессе* | ⏳ Запланировано |
| **08** | Git Submodules, Git LFS и Container Registry в GitLab | 📄 *В процессе* | 📁 *В процессе* | ⏳ Запланировано |
| **09** | Стратегии ветвления в команде. Git Flow, GitLab Flow и Trunk-based | 📄 *В процессе* | 📁 *В процессе* | ⏳ Запланировано |
| **10** | Итоговый проект. Ревью и защита | 📄 *В процессе* | 📁 *В процессе* | ⏳ Запланировано |

---

## 🚀 Ключевые практические результаты (Лабораторные №1 и №2)

### 1. Архитектура и граф коммитов (`hello-git`)

В ходе выполнения работ был смоделирован полный жизненный цикл распределённой разработки:
* Инициализация репозитория, настройка `.gitignore` и Conventional Commits.
* Параллельная разработка в функциональных ветках `feature/payment` и `feature/notifications`.
* Трёхстороннее слияние и **ручное разрешение конфликта одновременного редактирования** в файле `features.txt`.
* Перебазирование ветки `feature/database` (`git rebase`) поверх `main` с разрешением конфликтов в `config.txt` и сохранением линейной истории.
* Релизное ветвление по методологии **Git Flow** (`release/v1.0`, `release/v1.1`) и создание версионного тега `v1.0.0`.

#### Граф истории коммитов проекта:
```text
* db5e3c8 chore(release): prepare release v1.1.0
* cf2ff56 feat: add third feature
* 258bab7 fix: update feature list with corrected feature
* 7b4c347 feat: add second feature
* 537688e feat: add first feature
* 0b2af84 chore(release): bump version to 1.0.0
* a4d04df feat(db): add database configuration
* 5b6c9b8 fix(db): change default database to MySQL
*   3f02434 merge: resolve conflict between payment and notifications
|\  
| * 0490dcd feat(notifications): add 2FA and notification system
* |   dabe573 Merge branch 'feature/payment'
|\ \  
| |/  
|/|   
| * a5a36e7 feat(payment): add payment and history features
|/  
* 97b6a99 feat: add features.txt with core features
* 960a80d chore: add .gitignore
* e8bdd1d feat: add README.md with project description
```

### 2. Синхронизация с GitLab

Все ветки и теги проектов также зеркалируются в удалённые репозитории на GitLab:  
* 🔗 **[gitlab.com/TheLegendMaster/hello-git](https://gitlab.com/TheLegendMaster/hello-git)** — проект лабораторных №1 и №2.
* 🔗 **[gitlab.com/TheLegendMaster/collab-project](https://gitlab.com/TheLegendMaster/collab-project)** — командный upstream-проект лабораторной №3.
* 🔗 **[gitlab.com/TheLegendMaster/collab-project-fork](https://gitlab.com/TheLegendMaster/collab-project-fork)** — форк разработчика лабораторной №3.

---

### 3. Совместная разработка и Forking Workflow (Лабораторная №3)

* Настроена схема совместной разработки с двумя удалёнными репозиториями: `origin` (личный форк) и `upstream` (основной проект команды).
* Разработан модуль калькулятора [`calc.py`](Лабораторные_работы/03_collab-project/calc.py) с базовыми арифметическими операциями.
* Смоделирован полный цикл **Merge Request**, рецензирования кода (**Code Review**), внесения правок по комментариям и слияния изменений в `main`.

#### Граф коммитов и слияний лабораторной №3:
```text
*   589c2f3 Merge branch 'feature/calculator' of collab-project-fork into main
|\  
| * cf2ec08 feat: add calculator module with core operations
|/  
*   b32cd92 Merge branch 'feature/add_contributor' of collab-project-fork into main
|\  
| * 3577d8b fix: update contributors table format and group information
| * 48cdfb7 docs: add self to contributors
|/  
* 821c5b4 docs: add CONTRIBUTORS.md and update README.md
* 1f98de5 docs: initial commit
```

---

### 4. Управление историей коммитов (Лабораторная №4)

* Исследованы режимы отмены: `git reset` (`--soft`, `--mixed`, `--hard`), `git revert`, `git restore` и `git commit --amend`.
* Отработано интерактивное перебазирование (`git rebase -i`): склеивание коммитов (`squash`), изменение сообщений (`reword`) и исключение секретов.
* Выполнена очистка репозитория от ошибочно добавленного файла с паролем `secret.txt` через `git filter-branch`.
* Отработана принудительная безопасная отправка истории с флагом `--force-with-lease`.

#### Граф коммитов лабораторной №4:
```text
* 5d12c19 feat(notifications): add advanced notification service
* 81efd0b docs: update payment gateway documentation
* fa6152c feat: add database models
* ed5ea02 docs: update user authentication specifications
| * 486f4c7 fix: accidentally added database password
| * 67dc5fd feat(notifications): add advanced notification service
| * 2fc2d15 feat: add payment gateway integration
|/  
* 74fcd3a feat: initial structure for clean history
* eec851a feat: add line 5 with extra details
* af1dfed feat: add line 4
* d9a955c feat: add lines 1 to 3 combined with squash
```

---

### 5. Автоматизация разработки: Git Hooks и GitLab CI/CD (Лабораторная №5)

* Разработан комплекс клиентских перехватчиков (`.githooks/`):
  * `pre-commit`: предотвращение коммитов с синтаксическими ошибками Python и утечками паролей/токенов.
  * `commit-msg`: строгая валидация формата сообщений по спецификации Conventional Commits.
  * `post-commit`: автоматическое ведение журнала фиксаций в `commit.log`.
* Сконфигурирован многостадийный пайплайн `.gitlab-ci.yml` (`lint`, `test`, `security`, `build`) с сохранением артефактов `dist/`.
* Добавлен модуль модульного тестирования `test.py` (`unittest`) и бейдж статуса пайплайна.

---

## 📂 Структура репозитория

```text
VSC/
├── README.md                          # Главный навигатор по курсу (данный файл)
├── .gitignore                         # Правила игнорирования временных файлов
├── Отчеты/                            # Академические отчёты по лабораторным работам
│   ├── Отчет_Лабораторная_1.md        # Отчёт №1 (SSH, настройка, базовые команды)
│   ├── Отчет_Лабораторная_2.md        # Отчёт №2 (ветвление, конфликты, merge, rebase)
│   ├── Отчет_Лабораторная_3.md        # Отчёт №3 (удалённые репозитории, Fork, MR, Code Review)
│   ├── Отчет_Лабораторная_4.md        # Отчёт №4 (rebase, reset, revert, squash, force-with-lease)
│   └── Отчет_Лабораторная_5.md        # Отчёт №5 (Git Hooks, .gitlab-ci.yml, автоматизация)
├── Лабораторные_работы/               # Практические материалы и файлы проектов
│   ├── 01_02_hello-git/               # Проект hello-git (лабораторные 1 и 2)
│   │   ├── README.md
│   │   ├── features.txt
│   │   ├── config.txt
│   │   ├── version.txt
│   │   ├── diff.txt
│   │   └── history.txt
│   ├── 03_collab-project/             # Проект совместной разработки (лабораторная 3)
│   │   ├── README.md
│   │   ├── CONTRIBUTORS.md
│   │   ├── MY_CONTRIBUTION.md
│   │   ├── calc.py
│   │   └── history.txt
│   ├── 04_history-management/         # Проект управления историей (лабораторная 4)
│   │   ├── module1.txt ... module5.txt
│   │   ├── app.py, data.txt
│   │   ├── file_rebase.txt
│   │   └── history.txt
│   └── 05_hooks-and-cicd/             # Проект автоматизации и CI/CD (лабораторная 5)
│       ├── .githooks/ (pre-commit, commit-msg, post-commit, pre-push)
│       ├── scripts/install-hooks.sh
│       ├── .gitlab-ci.yml
│       ├── app.py, test.py
│       ├── requirements.txt
│       ├── commit.log
│       └── history.txt
└── Задания/                           # Учебный план и методические указания
    ├── 0000_plan.md
    ├── 0102_lab.md
    ├── 0202_lab.md
    ├── 0302_lab.md
    ├── 0402_lab.md
    ├── 0502_lab.md
    └── ...
```

---

## 🛠 Полезные команды для проверки

```bash
# Клонирование репозитория
git clone git@github.com:TheLegendMaster2023/VSC.git
cd VSC

# Просмотр дерева коммитов
git log --graph --oneline --all

# Просмотр веток
git branch -a
```

---

<p align="center">
  <b>СКФУ • 2026</b>
</p>
