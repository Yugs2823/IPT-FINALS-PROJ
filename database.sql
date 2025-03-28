CREATE DATABASE IF NOT EXISTS my_database;
USE my_database;

-- Admin Table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(50) NOT NULL
);

-- Lakers Players Table
CREATE TABLE IF NOT EXISTS players (
    jersey_number INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    college VARCHAR(100),
    salary VARCHAR(50)
);

-- Admins or Lakers Managers
INSERT INTO users (username, password) VALUES
    ('Miguel Hufancia', 'password1'),
    ('Arnold Alisangco', 'password2'),
    ('Enzo Talampas', 'password3'),
    ('Nathaniel Torre', 'password4')
ON DUPLICATE KEY UPDATE username=username;

-- Lakers Roster
INSERT INTO players (jersey_number, name, college, salary) VALUES
    (2, 'Jarred Vanderbilt', 'Kentucky', '$10,714,286'),
    (4, 'Dalton Knecht', 'Tennessee', '$3,819,120'),
    (7, 'Gabe Vincent', 'UC Santa Barbara', '$11,000,000'),
    (9, 'Bronny James', 'USC', '$1,157,153'),
    (10, 'Christian Koloko', 'Arizona', '--'),
    (11, 'Jaxson Hayes', 'Texas', '$2,463,946'),
    (14, 'Maxi Kleber', '--', '$11,000,000'),
    (15, 'Markieff Morris', 'Kansas', '$2,087,519'),
    (17, 'Dorian Finney-Smith', 'Florida', '$14,924,168'),
    (18, 'Shake Milton', 'SMU', '$2,875,000'),
    (23, 'LeBron James', '--', '$48,728,845'),
    (25, 'Austin Reaves', 'Oklahoma', '$12,976,362'),
    (27, 'Alex Len', 'Maryland', '$2,087,519'),
    (28, 'Rui Hachimura', 'Gonzaga', '$17,000,000'),
    (30, 'Jordan Goodwin', 'Saint Louis', '--'),
    (55, 'Trey Jemison III', 'UAB', '--'),
    (77, 'Luka Dončić', '--', '$43,031,940')
ON DUPLICATE KEY UPDATE name=name;

