# Проект "Servis upravleniya rassylkami (SUR)" - Сервис управления рассылками

## Описание:
 Проект "SUR" - это проект на Python, 
 передставляющи собой сервис управления рассылками
 
## Установка:
 1. Клонируйте репозиторий:
 ```
 git clone https://github.com/Irina-Sudeykina/sur.git
 
 ```

 2. Установите зависимости:
 ```
 pip install -r requirements.txt
 ```

## Использование:
 
### Контроллер CategoryListView(ListView) ###
Контроллер для рендера страницы с категориями продуктов

### Контроллер CategoryDetailView(ListView) ###
Контроллер для рендера страницы продуктов определенной категории

### Контроллер ProductListView(ListView) ###
Контроллер для рендера главной страницы

### Контроллер ProducDetailView(DetailView) ###
Контроллер для рендера страницы с товаром

### Контроллер ProductCreateView(CreateView) ###
Контроллер для рендера страницы создания товара

### Контроллер ProductUpdateView(UpdateView) ###
Контроллер для рендера страницы редактирования товара

### Контроллер ProductDeleteView(DeleteView) ###
Контроллер для рендера страницы удаления товара

### Контроллер ContactsView(View) ###
Контроллер для рендера страницы "Контакты"<br>
Осуществляет прием информаци с формы "Свяжитесь с нами":<br>
    - name - Имя<br>
    - phone - Телефон<br>
    - message - Сообщение<br>


### Контроллер BlogPostListView(ListView) ###
Контроллер для рендера главной блога

### Контроллер BlogPostDetailView(DetailView) ###
Контроллер для рендера поста блога

### Контроллер BlogPostCreateView(CreateView) ###
Контроллер для создания поста блога

### Контроллер BlogPostUpdateView(UpdateView) ###
Контроллер для редактирования поста блога

### Контроллер BlogPostDeleteView(DeleteView) ###
Контроллер для удаления поста блога

### Контроллер RegisterView(CreateView) ###
Контроллер регистрации

### Контроллер CustomLoginView(LoginView) ###
Контроллер для входа на сайт


### Модель Product: ###
name - наименование,<br>
description - описание,<br>
image - изображение,<br>
category - категория,<br>
price - цена за покупку,<br>
created_at - дата создания,<br>
updated_at - дата последнего изменения.<br>
is_publication - статус публикации<br>
owner - владелец<br>


### Модель Category: ###
name - наименование,<br>
description - описание.<br>


### Модель BlogPost: ###
title - заголовок,<br>
description - содержимое,<br>
image - изображение,<br>
created_at - дата создания,<br>
is_publication - признак публикации,<br>
views_count - количество просмотров.<br>


### Модель CustomUser: ###
Добавлены поля:<br>
email - email,<br>
avatar - аватар,<br>
phone_number - телефон,<br>
country - страна<br>


### Форма ProductForm: ###
Форма для отображения и валидации при создании/редактировании продукта

### Форма BlogPostForm: ###
Форма для отображения и валидации при создании/редактировании поста блога

### Форма CustomUserCreationForm: ###
Форма регистрации

### Форма CustomLoginForm: ###
Форма для входа на сайт

### Функция get_products_from_cache ###
Получет данные по продуктам из кеша, 
если кеш пуст, то получает данные из БД

### Класс CategoryService ###
Класс для получения списка продуктов в заданной категории

## Загрузка фикстур: ###
Способ 1: - загрузка из файла<br>
Зайдите в Django shell и выполните:
```
Product.objects.all().delete()
Category.objects.all().delete()

BlogPost.objects.all().delete()
```
В терминале выполните:
```
python manage.py loaddata catalog_fixture.json --format json
python manage.py loaddata blogpost_fixture.json --format json
```
Способ 2 - используя кастомные команды<br>
В терминале выполните:
```
python manage.py add_products
python manage.py add_blogposts
```


## Запуск сервера:
В терминале выполните:
 ```
python manage.py runserver
 ```
Для остановки нажмите Ctrl + C

## Документация:

## Лицензия:
Проект распространяется под [лицензией MIT](LICENSE).
