CREATE DATABASE IF NOT EXISTS `debatsido`;

-- Création de la table citation --
CREATE TABLE `debatsido`.`citation` (
  `idcitation` INT NOT NULL AUTO_INCREMENT,
  `cnom` VARCHAR(500) NOT NULL,
  `texte` VARCHAR(1000) NULL,
  `cnature` VARCHAR(45) NOT NULL,
  `completude` FLOAT NOT NULL,
  PRIMARY KEY (`idcitation`));

  -- Création de la table lien citation --
  CREATE TABLE `debatsido`.`lien_citation` (
  `positionnement` VARCHAR(10) NOT NULL,
  `id_cit1` INT NOT NULL,
  `id_cit2` INT NOT NULL,
  PRIMARY KEY (`id_cit1`, `id_cit2`),
  INDEX `fk_id_cit2_idx` (`id_cit2` ASC),
  CONSTRAINT `fk_id_cit1`
    FOREIGN KEY (`id_cit1`)
    REFERENCES `debatsido`.`citation` (`idcitation`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_id_cit2`
    FOREIGN KEY (`id_cit2`)
    REFERENCES `debatsido`.`citation` (`idcitation`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

    -- Création table theme --
    CREATE TABLE  `debatsido`.`theme` (
  `idtheme` INT NOT NULL AUTO_INCREMENT,
  `tnom` VARCHAR(60) NOT NULL,
  PRIMARY KEY (`idtheme`));

  -- Création table lien theme et citation --
  CREATE TABLE `debatsido`.`lien_citation_theme` (
  `idcit_fk` INT NOT NULL,
  `idtheme_fk` INT NOT NULL,
  PRIMARY KEY (`idcit_fk`, `idtheme_fk`),
  INDEX `idtheme_fk_idx` (`idtheme_fk` ASC),
  CONSTRAINT `idCit_fk`
    FOREIGN KEY (`idcit_fk`)
    REFERENCES `debatsido`.`citation` (`idcitation`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idtheme_fk`
    FOREIGN KEY (`idtheme_fk`)
    REFERENCES `debatsido`.`theme` (`idtheme`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

    -- Création table medium --
    CREATE TABLE  `debatsido`.`medium` (
  `idmedium` INT NOT NULL,
  `date` DATETIME NULL,
  `mnature` VARCHAR(45) NOT NULL,
  `lien` VARCHAR(100) NULL,
  `mnom` VARCHAR(100) NULL DEFAULT NULL ,
  `fiabilite` INT NULL,
  `mtitre` VARCHAR(200) NULL,
  PRIMARY KEY (`idmedium`));

  -- Création table lien citation et medium --
  CREATE TABLE `debatsido`.`lien_citation_medium` (
  `idcitation_fk` INT NOT NULL,
  `idmedium_fk` INT NOT NULL,
  `primaire` TINYINT NOT NULL,
  PRIMARY KEY (`idcitation_fk`, `idmedium_fk`),
  INDEX `idmed_fk_idx` (`idmedium_fk` ASC),
  CONSTRAINT `idcitation_fk`
    FOREIGN KEY (`idcitation_fk`)
    REFERENCES `debatsido`.`citation` (`idcitation`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idmed_fk`
    FOREIGN KEY (`idmedium_fk`)
    REFERENCES `debatsido`.`medium` (`idmedium`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

-- Création table personne --
CREATE TABLE `debatsido`.`personne` (
  `idpersonne` INT NOT NULL AUTO_INCREMENT,
  `pnom` VARCHAR(45) NOT NULL,
  `statut` VARCHAR(45) NOT NULL,
  `lien_biographie` VARCHAR(60) NULL,
  PRIMARY KEY (`idpersonne`));

  -- Création table lien medium et personne (si la personne est auteur)--
  CREATE TABLE `debatsido`.`auteur` (
  `idmedium_fk` INT NOT NULL,
  `idpersonne_fk` INT NOT NULL,
  PRIMARY KEY (`idmedium_fk`, `idpersonne_fk`),
  INDEX `idpersonne_fk_idx` (`idpersonne_fk` ASC),
  CONSTRAINT `idmedium_fk`
    FOREIGN KEY (`idmedium_fk`)
    REFERENCES `debatsido`.`medium` (`idmedium`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idpersonne_fk`
    FOREIGN KEY (`idpersonne_fk`)
    REFERENCES `debatsido`.`personne` (`idpersonne`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

    -- Création lien citation et personne (si la personne est partie prenante)--
    CREATE TABLE `debatsido`.`partie_prenante` (
  `idcitation_fk` INT NOT NULL,
  `idpersonne_fk` INT NOT NULL,
  `est_partie_prenante` TINYINT NOT NULL,
  PRIMARY KEY (`idcitation_fk`, `idpersonne_fk`),
  INDEX `idpersonne_fk_idx` (`idpersonne_fk` ASC),
  CONSTRAINT `idcita_fk`
    FOREIGN KEY (`idcitation_fk`)
    REFERENCES `debatsido`.`citation` (`idcitation`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idpers_fk`
    FOREIGN KEY (`idpersonne_fk`)
    REFERENCES `debatsido`.`personne` (`idpersonne`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

    -- Modifications tables --
    
ALTER TABLE `debatsido`.`lien_citation` 
DROP FOREIGN KEY `fk_id_cit1`;
ALTER TABLE `debatsido`.`lien_citation` 
ADD CONSTRAINT `fk_id_cit1`
  FOREIGN KEY (`id_cit1`)
  REFERENCES `debatsido`.`citation` (`idcitation`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;

ALTER TABLE `debatsido`.`lien_citation` 
DROP FOREIGN KEY `fk_id_cit2`;
ALTER TABLE `debatsido`.`lien_citation` 
ADD CONSTRAINT `fk_id_cit2`
  FOREIGN KEY (`id_cit2`)
  REFERENCES `debatsido`.`citation` (`idcitation`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;