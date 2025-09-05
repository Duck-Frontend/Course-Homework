CREATE DATABASE homework_db;

\c homework_db;

CREATE TABLE Employees(
    id SERIAL PRIMARY KEY,
    name varchar(128) not null,
    position varchar(128) not null,
    department varchar(128) not null,
    salary decimal(8,2)
);

INSERT INTO Employees (name, position, department, salary) VALUES
('Иван Иванов', 'Разработчик', 'IT', 85000.50),
('Мария Петрова', 'Менеджер проектов', 'IT', 92000.00),
('Алексей Сидоров', 'Аналитик', 'Финансы', 78000.75),
('Елена Козлова', 'Бухгалтер', 'Финансы', 65000.00),
('Дмитрий Волков', 'HR-специалист', 'Отдел кадров', 58000.25),
('Ольга Орлова', 'Маркетолог', 'Маркетинг', 72000.50),
('Сергей Новиков', 'Тестировщик', 'IT', 68000.00),
('Анна Смирнова', 'Дизайнер', 'Маркетинг', 75000.00),
('Павел Белов', 'Системный администратор', 'IT', 89000.00),
('Ирина Зайцева', 'Менеджер по продажам', 'Продажи', 95000.00);

ALTER TABLE Employees ADD COLUMN HideDate DATE;

UPDATE Employees SET HideDate = '2024-01-15' WHERE name = 'Иван Иванов';
UPDATE Employees SET HideDate = '2024-02-20' WHERE name = 'Мария Петрова';
UPDATE Employees SET HideDate = '2024-03-10' WHERE name = 'Алексей Сидоров';
UPDATE Employees SET HideDate = '2024-01-30' WHERE name = 'Елена Козлова';
UPDATE Employees SET HideDate = '2024-04-05' WHERE name = 'Дмитрий Волков';
UPDATE Employees SET HideDate = '2024-02-14' WHERE name = 'Ольга Орлова';
UPDATE Employees SET HideDate = '2024-05-22' WHERE name = 'Сергей Новиков';
UPDATE Employees SET HideDate = '2024-03-18' WHERE name = 'Анна Смирнова';
UPDATE Employees SET HideDate = '2024-06-08' WHERE name = 'Павел Белов';
UPDATE Employees SET HideDate = '2024-01-08' WHERE name = 'Ирина Зайцева';

SELECT * FROM Employees WHERE position LIKE '%Менеджер%';

SELECT * FROM Employees WHERE salary > 5000;

SELECT * FROM Employees WHERE department LIKE '%Sales%';

SELECT AVG(salary) as average_salary FROM Employees;

DROP TABLE Employees;
