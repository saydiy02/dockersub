USE sir_db;

CREATE TABLE mytable (
  `user` VARCHAR(255), 
  `points` INT, 
  `datetime_stamp` DATETIME, 
  PRIMARY KEY (`points`)
);

INSERT INTO mytable (`user`, `points`, `datetime_stamp`) VALUES
('minah', 123, '2022-04-07 11:09:00'), 
('abu', 345, '2022-02-22 18:55:00'), 
('amin', 341, '2022-04-29 14:30:00');
