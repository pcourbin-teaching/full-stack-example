LOAD DATA INFILE "/var/lib/mysql-files/Source_Type.csv"
INTO TABLE `Source_Type`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA INFILE "/var/lib/mysql-files/Source.csv"
REPLACE
INTO TABLE `Source`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES

(@id, @title, @text, @url, @date, @id_type, @reliability, @date_update)
SET
id = nullif(@id,''),
title = nullif(@title,''),
text = nullif(@text,''),
url = nullif(@url,''),
date = IF(CHAR_LENGTH((@date)) = 0, NULL, STR_TO_DATE(@date,'%d/%m/%Y')),
id_type = nullif(@id_type,''),
reliability = nullif(@reliability,''),
date_update = IF(CHAR_LENGTH((@date_update)) = 0, now(), @date_update)
;

LOAD DATA INFILE "/var/lib/mysql-files/Quote_Type.csv"
INTO TABLE `Quote_Type`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;


LOAD DATA INFILE "/var/lib/mysql-files/Quote.csv"
REPLACE
INTO TABLE `Quote`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES

(@id, @title, @text, @id_type, @date_update)
SET
id = nullif(@id,''),
title = nullif(@title,''),
text = nullif(@text,''),
id_type = nullif(@id_type,''),
date_update = IF(CHAR_LENGTH((@date_update)) = 0, now(), @date_update)
;

LOAD DATA INFILE "/var/lib/mysql-files/QuoteLink_Type.csv"
INTO TABLE `QuoteLink_Type`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA INFILE "/var/lib/mysql-files/QuoteLink.csv"
REPLACE
INTO TABLE `QuoteLink`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES

(@id_quote_main, @id_quote_support, @id_type, @date_update)
SET
id_quote_main = nullif(@id_quote_main,''),
id_quote_support = nullif(@id_quote_support,''),
id_type = nullif(@id_type,''),
date_update = IF(CHAR_LENGTH((@date_update)) = 0, now(), @date_update)
;

LOAD DATA INFILE "/var/lib/mysql-files/Theme.csv"
INTO TABLE `Theme`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA INFILE "/var/lib/mysql-files/Entity.csv"
REPLACE
INTO TABLE `Entity`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES

(@id, @type, @name, @link, @photo, @date_update)
SET
id = nullif(@id,''),
type = nullif(@type,''),
name = nullif(@name,''),
link = nullif(@link,''),
photo = nullif(@photo,''),
date_update = IF(CHAR_LENGTH((@date_update)) = 0, now(), @date_update)
;

LOAD DATA INFILE "/var/lib/mysql-files/Person.csv"
REPLACE
INTO TABLE `Person`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES

(@id, @surname, @role, @date_update)
SET
id = nullif(@id,''),
surname = nullif(@surname,''),
role = nullif(@role,''),
date_update = IF(CHAR_LENGTH((@date_update)) = 0, now(), @date_update)
;

LOAD DATA INFILE "/var/lib/mysql-files/SourceAuthor.csv"
INTO TABLE `SourceAuthor`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA INFILE "/var/lib/mysql-files/SourceQuote.csv"
INTO TABLE `SourceQuote`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA INFILE "/var/lib/mysql-files/QuoteTheme.csv"
INTO TABLE `QuoteTheme`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

SELECT * FROM Quote q JOIN Quote_Type qt ON q.id_type = qt.id JOIN QuoteTheme qth ON qth.id_quote = q.id JOIN Theme th ON qth.id_theme = th.id;
SELECT * FROM Entity e JOIN QuoteAuthor qa ON e.id = qa.id_author JOIN Quote q ON qa.id_quote = q.id;
SELECT * FROM Entity e JOIN SourceAuthor sa ON e.id = sa.id_author JOIN Source s ON sa.id_source = s.id JOIN Source_Type st ON s.id_type = st.id;
SELECT q1.title, q2.title, qlt.title FROM Quote q1 JOIN QuoteLink ql ON q1.id = ql.id_quote_main JOIN Quote q2 ON ql.id_quote_support = q2.id JOIN QuoteLink_Type qlt ON ql.id_type = qlt.id;
