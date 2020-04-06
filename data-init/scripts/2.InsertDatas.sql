LOAD DATA INFILE "/var/lib/mysql-files/referenceType.csv"
INTO TABLE `referenceType`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA INFILE "/var/lib/mysql-files/reference.csv"
REPLACE
INTO TABLE `reference`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES

(@id, @title, @details, @url, @date, @typeID, @reliability, @dateUpdate)
SET
id = nullif(@id,''),
title = nullif(@title,''),
details = nullif(@details,''),
url = nullif(@url,''),
date = IF(CHAR_LENGTH((@date)) = 0, NULL, STR_TO_DATE(@date,'%d/%m/%Y')),
typeID = nullif(@typeID,''),
reliability = nullif(@reliability,''),
dateUpdate = IF(CHAR_LENGTH((@dateUpdate)) = 0, now(), @dateUpdate)
;

LOAD DATA INFILE "/var/lib/mysql-files/quoteType.csv"
INTO TABLE `quoteType`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;


LOAD DATA INFILE "/var/lib/mysql-files/quote.csv"
REPLACE
INTO TABLE `quote`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES

(@id, @title, @details, @typeID, @dateUpdate)
SET
id = nullif(@id,''),
title = nullif(@title,''),
details = nullif(@details,''),
typeID = nullif(@typeID,''),
dateUpdate = IF(CHAR_LENGTH((@dateUpdate)) = 0, now(), @dateUpdate)
;

LOAD DATA INFILE "/var/lib/mysql-files/quoteLinkType.csv"
INTO TABLE `quoteLinkType`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA INFILE "/var/lib/mysql-files/quoteLink.csv"
REPLACE
INTO TABLE `quoteLink`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES

(@quoteMainID, @quoteSupportID, @typeID, @dateUpdate)
SET
quoteMainID = nullif(@quoteMainID,''),
quoteSupportID = nullif(@quoteSupportID,''),
typeID = nullif(@typeID,''),
dateUpdate = IF(CHAR_LENGTH((@dateUpdate)) = 0, now(), @dateUpdate)
;

LOAD DATA INFILE "/var/lib/mysql-files/theme.csv"
INTO TABLE `theme`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA INFILE "/var/lib/mysql-files/protagonist.csv"
REPLACE
INTO TABLE `protagonist`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES

(@id, @type, @name, @link, @photo, @dateUpdate)
SET
id = nullif(@id,''),
type = nullif(@type,''),
name = nullif(@name,''),
link = nullif(@link,''),
photo = nullif(@photo,''),
dateUpdate = IF(CHAR_LENGTH((@dateUpdate)) = 0, now(), @dateUpdate)
;

LOAD DATA INFILE "/var/lib/mysql-files/person.csv"
REPLACE
INTO TABLE `person`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES

(@id, @surname, @role, @dateUpdate)
SET
id = nullif(@id,''),
surname = nullif(@surname,''),
role = nullif(@role,''),
dateUpdate = IF(CHAR_LENGTH((@dateUpdate)) = 0, now(), @dateUpdate)
;

LOAD DATA INFILE "/var/lib/mysql-files/referenceAuthor.csv"
INTO TABLE `referenceAuthor`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA INFILE "/var/lib/mysql-files/quoteReference.csv"
INTO TABLE `quoteReference`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA INFILE "/var/lib/mysql-files/quoteTheme.csv"
INTO TABLE `quoteTheme`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

SELECT * FROM quote q JOIN quoteType qt ON q.typeID = qt.id JOIN quoteTheme qth ON qth.quoteID = q.id JOIN theme th ON qth.themeID = th.id;
SELECT * FROM protagonist e JOIN quoteAuthor qa ON e.id = qa.authorID JOIN quote q ON qa.quoteID = q.id;
SELECT * FROM protagonist e JOIN referenceAuthor sa ON e.id = sa.authorID JOIN reference s ON sa.referenceID = s.id JOIN referenceType st ON s.typeID = st.id;
SELECT q1.title, q2.title, qlt.title FROM quote q1 JOIN quoteLink ql ON q1.id = ql.quoteMainID JOIN quote q2 ON ql.quoteSupportID = q2.id JOIN quoteLinkType qlt ON ql.typeID = qlt.id;


SELECT q.id as quoteID, q.title as title, q.details as details, q.typeID as typeID, qt.title as typeTitle, q.dateUpdate as dateUpdate FROM quote q JOIN quoteType qt ON q.typeID = qt.id;
SELECT t.id as id, t.title as title FROM theme t JOIN quoteTheme qt ON t.id = qt.themeID WHERE qt.quoteID = 51;
SELECT r.id, r.title, r.details, r.url, r.date, r.typeID, rt.title, r.reliability, r.dateUpdate FROM reference r JOIN quoteReference qr ON r.id = qr.referenceID JOIN referenceType rt ON r.typeID = rt.id WHERE qr.quoteID = 3;

SELECT p.id, p.type, p.name, p.link, p.photo, p.dateUpdate FROM protagonist p JOIN referenceAuthor ra ON p.id = ra.authorID JOIN reference r ON r.id = ra.referenceID WHERE r.id = 1;
SELECT pe.id, pe.surname, pe.role, pe.dateUpdate FROM protagonist pr JOIN person pe ON pr.id = pe.id WHERE pr.id = 1;
SELECT pe.id, pe.surname, pe.role, pe.dateUpdate FROM protagonist pr JOIN person pe ON pr.id = pe.id JOIN quoteAuthor qa ON qa.authorID = pr.id;
SELECT * FROM company;

SELECT q.id, q.title, q.details, q.typeID, qt.title as typeTitle, q.dateUpdate FROM quote q JOIN quoteType qt ON q.typeID JOIN quoteLink ql ON ql.quoteSupportID = q.id WHERE ql.quoteMainID = 2;
SELECT ql.quoteMainID, ql.quoteSupportID, ql.typeID, qlt.title, ql.dateUpdate FROM quoteLink ql JOIN quoteLinkType qlt ON ql.typeID = qlt.id WHERE ql.quoteSupportID = 2;