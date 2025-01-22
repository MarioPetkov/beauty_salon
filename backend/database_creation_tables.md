# database_creation_tables.md
# Current structure of the database
-- Таблица за клиентите (Google профил + информация за клиента)
CREATE TABLE customers (
    id SERIAL PRIMARY KEY NOT NULL,
    google_id VARCHAR(255) UNIQUE NOT NULL,  -- Уникален идентификатор за Google профил
    email VARCHAR(255) UNIQUE NOT NULL,  -- Емейл адрес от Google
    full_name VARCHAR(100),  -- Пълно име от Google профил
    profile_picture TEXT,  -- Линк към профилна снимка
    phone_number VARCHAR(15) UNIQUE NOT NULL,  -- Телефонен номер на клиента
    birth_date DATE,  -- Рождена дата
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Дата на създаване
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Дата на последна актуализация
);

-- Таблица за служителите
CREATE TABLE employees (
    id SERIAL PRIMARY KEY NOT NULL,
    first_name VARCHAR(100) NOT NULL,  -- Име на служителя
    last_name VARCHAR(100) NOT NULL,  -- Фамилия на служителя
    phone_number VARCHAR(15) UNIQUE NOT NULL,  -- Телефонен номер на служителя
    birth_date DATE,  -- Рождена дата
    hire_date DATE DEFAULT CURRENT_DATE,  -- Дата на наемане
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Дата на създаване
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Дата на последна актуализация
    category_id INT REFERENCES categories(id) ON DELETE SET NULL,  -- Връзка към категория
    is_active BOOLEAN DEFAULT TRUE  -- Флаг за активност
);

-- Таблица за услугите
CREATE TABLE services (
    id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(100) NOT NULL,  -- Име на услугата
    employee_id INT REFERENCES employees(id) ON DELETE SET NULL,  -- Връзка към служителя
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),  -- Цена на услугата
    description TEXT,  -- Описание на услугата
    duration INT,  -- Продължителност на услугата в минути
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Дата на създаване
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Дата на последна актуализация
);

-- Таблица за записаните часове
CREATE TABLE appointments (
    id SERIAL PRIMARY KEY NOT NULL,
    customer_id INT REFERENCES customers(id) ON DELETE CASCADE,  -- Връзка към клиента
    employee_id INT REFERENCES employees(id) ON DELETE SET NULL,  -- Връзка към служителя
    service_id INT REFERENCES services(id) ON DELETE CASCADE,  -- Връзка към услугата
    appointment_date DATE NOT NULL,  -- Дата на записа
    appointment_hour TIME NOT NULL,  -- Час на записа
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),  -- Цена на услугата
    status VARCHAR(50) DEFAULT 'pending' CHECK (status IN ('pending', 'confirmed', 'completed', 'cancelled')),  -- Статус на записа
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Дата на създаване
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Дата на последна актуализация
    cancellation_reason TEXT,  -- Причина за отказ
    notes TEXT,  -- Допълнителни коментари
);

-- Таблица за категориите услуги
CREATE TABLE categories (
    id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(100) NOT NULL UNIQUE,  -- Например: "Маникюр", "Фризьорство", "Козметика"
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Добавяне на референция към categories в таблицата services
ALTER TABLE services 
    ADD COLUMN category_id INT REFERENCES categories(id) ON DELETE SET NULL;

-- Добавяне на референция към categories в таблицата employees
ALTER TABLE employees 
    ADD COLUMN category_id INT REFERENCES categories(id) ON DELETE SET NULL;

-- Създаване на индекс за по-бързо търсене по категория
CREATE INDEX idx_services_category ON services(category_id);
CREATE INDEX idx_employees_category ON employees(category_id);

-- Добавяне на някои примерни категории
INSERT INTO categories (name, description) VALUES
    ('Маникюр', 'Услуги за нокти'),
    ('Фризьорство', 'Подстригване, боядисване и стилизиране на коса'),
    ('Козметика', 'Козметични процедури за лице и тяло'),
    ('Масаж', 'Различни видове масажи');

