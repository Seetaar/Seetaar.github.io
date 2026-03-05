# Лабораторная работа №1: Создание статического сайта

## Цель работы

- Освоить процесс создания статического сайта с использованием генератора документации MkDocs.
- Научиться организовывать структуру документации проекта (портфолио лабораторных работ).
- Изучить базовые принципы работы с системой контроля версий Git и платформой GitHub.
- Развернуть статический сайт с использованием механизма GitHub Pages на домене вида username.github.io.
- Освоить базовую настройку темы оформления и конфигурационного файла mkdocs.yml.

## Задание

1. Выбрать и подключить тему оформления.
2. Настроить файл mkdocs.yml.
3. Создать структуру страниц.
4. Обеспечить корректную навигацию по сайту.
5. Выполнить повторную сборку и публикацию сайта.

## Структура проекта

- Seetaar.github.io
    - mkdocs.yml
    - src
        - index.md
        - about.md
        - labs
            - lab1.md
            - lab2.md
            - lab3.md

## Реализация

Файл `mkdocs.yml`:

```yaml
site_name: "Портфолио | Seetaar"
site_description: "Учебное портфолио студента ITMO University"
site_author: "Seetaar"
site_url: "https://Seetaar.github.io"

docs_dir: src
site_dir: docs

theme:
  name: material
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: deep-purple
      accent: teal
      toggle:
        icon: material/brightness-7
        name: Перейти в тёмную тему
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: deep-purple
      accent: teal
      toggle:
        icon: material/brightness-4
        name: Перейти в светлую тему
  font:
    text: Roboto
    code: JetBrains Mono
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.indexes
    - search.highlight
    - content.code.copy
    - content.code.annotate

nav:
  - Главная: index.md
  - Об авторе: about.md
  - Лабораторные работы:
      - labs/labs_index.md
      - "Лаба 1": labs/lab1.md
      - "Лаба 2": labs/lab2.md
      - "Лаба 3": labs/lab3.md


markdown_extensions:
  - pymdownx.highlight:
      anchor_linenums: true
      line_spans: __span
      pygments_lang_class: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
  - pymdownx.details
  - attr_list
  - md_in_html
  - tables
  - admonition
  - def_list
```