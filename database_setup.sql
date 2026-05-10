-- 1. Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS planflow_db;
USE planflow_db;

-- 2. Create the Users table
CREATE TABLE Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    daily_standard_capacity INT NOT NULL DEFAULT 8
);

-- 3. Create the Tasks table (with urgency_level column)
CREATE TABLE Tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    task_name VARCHAR(255) NOT NULL,
    estimated_duration INT NOT NULL,
    mental_difficulty INT CHECK (mental_difficulty BETWEEN 1 AND 5),
    urgency_level INT DEFAULT 1 CHECK (urgency_level BETWEEN 1 AND 3),
    status ENUM('Pending', 'Completed') DEFAULT 'Pending',
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE
);

-- 4. Create the Daily_Logs table
CREATE TABLE Daily_Logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    log_date DATE NOT NULL,
    user_id INT,
    planned_total_duration INT DEFAULT 0,
    physical_activity_score INT,
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE
);

-- 5. Insert Mock Data (Test Scenarios)
-- Users: Tahir (Standard), Alex (Lower Capacity), Sarah (High Capacity)
INSERT INTO Users (name, daily_standard_capacity) VALUES 
('Tahir', 8),
('Alex', 6),
('Sarah', 10);

-- Tasks for Tahir (User 1) - High Load & High Difficulty
INSERT INTO Tasks (user_id, task_name, estimated_duration, mental_difficulty, urgency_level, status) VALUES
(1, 'IoT Smart Cold Storage Python Script', 180, 5, 3, 'Pending'),
(1, 'LeetCode Two-Pointer Practice', 120, 4, 2, 'Pending'),
(1, 'FC 26 Harrogate Town Career Match', 45, 1, 1, 'Completed'),
(1, 'Database ETL Pipeline Optimization', 150, 4, 3, 'Pending'),
(1, 'Read new Data Engineering article', 30, 2, 1, 'Pending');

-- Tasks for Alex (User 2) - Average Load
INSERT INTO Tasks (user_id, task_name, estimated_duration, mental_difficulty, urgency_level, status) VALUES
(2, 'UI Design for Mobile App', 240, 3, 2, 'Pending'),
(2, 'Client Sync Meeting', 60, 2, 3, 'Pending'),
(2, 'Fix CSS Layout Bugs', 120, 3, 1, 'Pending');

-- Tasks for Sarah (User 3) - Very Heavy Intellectual Load
INSERT INTO Tasks (user_id, task_name, estimated_duration, mental_difficulty, urgency_level, status) VALUES
(3, 'Train Deep Learning Model', 300, 5, 3, 'Pending'),
(3, 'Draft Research Paper', 200, 5, 2, 'Pending'),
(3, 'Review Pull Requests', 60, 4, 2, 'Completed');

-- Daily Logs for 2026-05-09
INSERT INTO Daily_Logs (log_date, user_id, planned_total_duration, physical_activity_score) VALUES
('2026-05-09', 1, 525, 8),
('2026-05-09', 2, 420, 2),
('2026-05-09', 3, 560, 4);