LOAD DATA INFILE "/secure_file_priv/Source_Type.csv"
INTO TABLE `Source_Type`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

SELECT * FROM `Source_Type`;
SELECT * FROM `Source`;
SELECT * FROM `Quote_Type`;
SELECT * FROM `Quote`;
SELECT * FROM `Theme`;
SELECT * FROM `Entity`;
SELECT * FROM `Person`;
SELECT * FROM Entity Natural Join Person;
SHOW VARIABLES LIKE "secure_file_priv";
SET secure_file_priv = "/secure_file_priv";

select a.idmedium_fk, a.idpersonne_fk from medium m join auteur a on m.idmedium = a.idmedium_fk join personne p on a.idpersonne_fk = p.idpersonne;

select * from citation c join partie_prenante pp on c.idcitation = pp.idcitation_fk join personne p on pp.idpersonne_fk = p.idpersonne;

select c.idcitation, m.idmedium from citation c join lien_citation_medium cm on c.idcitation = cm.idcitation_fk join medium m on cm.idmedium_fk = m.idmedium where c.idcitation <=57 order by c.idcitation;

select idtheme_fk, idcit_fk from citation c join lien_citation_theme cm on c.idcitation = cm.idcit_fk join theme t on cm.idtheme_fk = t.idtheme where c.idcitation <=57 order by c.idcitation;

select c1.idcitation, c2.idcitation, positionnement from citation c1 join lien_citation cm on cm.id_cit1 = c1.idcitation join citation c2 on cm.id_cit2 = c2.idcitation where c1.idcitation <=57 and  c2.idcitation <=57;


