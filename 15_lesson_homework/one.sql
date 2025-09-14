-- 1 задание
begin;
create table authors(
    id serial primary key,
    first_name varchar(128) not null,
    last_name varchar(128) not null
);

create table books(
    id serial primary key,
    title varchar(256) not null,
    public_year date,
    author_id int references authors(id)
);

create table sales(
    id serial primary key,
    book_id int references books(id),
    quantity int
);
end;

begin;
-- Заполнение таблицы authors
INSERT INTO authors (id, first_name, last_name) VALUES
(1, 'Лев', 'Толстой'),
(2, 'Фёдор', 'Достоевский'),
(3, 'Антон', 'Чехов'),
(4, 'Александр', 'Пушкин'),
(5, 'Михаил', 'Булгаков'),
(6, 'Николай', 'Гоголь'),
(7, 'Иван', 'Тургенев'),
(8, 'Александр', 'Солженицын'),
(9, 'Сергей', 'Довлатов'),
(10, 'Владимир', 'Набоков');

-- Заполнение таблицы books
INSERT INTO books (id, title, public_year, author_id) VALUES
(1, 'Война и мир', '1869-01-01', 1),
(2, 'Анна Каренина', '1877-01-01', 1),
(3, 'Преступление и наказание', '1866-01-01', 2),
(4, 'Идиот', '1869-01-01', 2),
(5, 'Вишнёвый сад', '1904-01-01', 3),
(6, 'Чайка', '1896-01-01', 3),
(7, 'Евгений Онегин', '1833-01-01', 4),
(8, 'Мастер и Маргарита', '1967-01-01', 5),
(9, 'Собачье сердце', '1925-01-01', 5),
(10, 'Мёртвые души', '1842-01-01', 6),
(11, 'Отцы и дети', '1862-01-01', 7),
(12, 'Архипелаг ГУЛАГ', '1973-01-01', 8),
(13, 'Зона', '1982-01-01', 9),
(14, 'Лолита', '1955-01-01', 10);

-- Заполнение таблицы sales
INSERT INTO sales (id, book_id, quantity) VALUES
(1, 1, 1500),
(2, 1, 800),
(3, 2, 1200),
(4, 3, 950),
(5, 3, 1100),
(6, 4, 750),
(7, 5, 600),
(8, 6, 550),
(9, 7, 1800),
(10, 8, 2500),
(11, 8, 1700),
(12, 9, 900),
(13, 10, 850),
(14, 11, 700),
(15, 12, 1300),
(16, 13, 950),
(17, 14, 1600),
(18, 14, 1200),
(19, 1, 650),
(20, 8, 1400);
end;

-- 2 задание
begin;
    select title, first_name, last_name from books inner join authors a on books.author_id = a.id;
    select title, first_name, last_name from authors left join books b on authors.id = b.author_id;
    select title, first_name, last_name from authors right join books b on authors.id = b.author_id;
end; -- Возможно я не понял задание, но ощущение будто нужно сделать одно и тоже

-- 3 задание
begin;
    select * from sales inner join books b on b.id = sales.book_id inner join authors a on a.id = b.author_id;
    select * from sales left join books b on b.id = sales.book_id left join authors a on a.id = b.author_id;
end;

-- 4 задание

begin;
    select a.first_name, a.last_name, sum(s.quantity) as total_books_sold from authors a inner join books b on a.id = b.author_id inner join sales s on b.id = s.book_id group by  a.id, a.first_name, a.last_name;
    select a.first_name, a.last_name, sum(s.quantity) as total_books_sold from authors a left join books b on a.id = b.author_id left join sales s on b.id = s.book_id group by  a.id, a.first_name, a.last_name;
end;

-- 5 задание

begin;
    select a.first_name, a.last_name, sum(s.quantity) as total_sold from authors a inner join books b on a.id = b.author_id inner join sales s on b.id = s.book_id group by a.id, a.first_name, a.last_name order by total_sold desc limit 1;
    select b.title, sum(s.quantity) as total_sold from books b inner join sales s on b.id = s.book_id group by b.id, b.title having sum(s.quantity) > (select avg(sq.total) from (select sum(quantity) as total from sales group by book_id) sq);
end;