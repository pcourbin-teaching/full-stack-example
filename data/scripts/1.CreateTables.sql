use spot;
set sql_safe_updates=0;

DROP TABLE IF EXISTS company;
DROP TABLE IF EXISTS person;
DROP TABLE IF EXISTS referenceAuthor;
DROP TABLE IF EXISTS quoteAuthor;
DROP TABLE IF EXISTS protagonist;
DROP TABLE IF EXISTS quoteReference;
DROP TABLE IF EXISTS quoteTheme;
DROP TABLE IF EXISTS theme;
DROP TABLE IF EXISTS quoteLink;
DROP TABLE IF EXISTS quoteLinkType;
DROP TABLE IF EXISTS quote;
DROP TABLE IF EXISTS quoteType;
DROP TABLE IF EXISTS reference;
DROP TABLE IF EXISTS referenceType;

CREATE TABLE `referenceType` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `title` TEXT NOT NULL,
  PRIMARY KEY (`id`)
) CHARACTER SET utf8mb4;

CREATE TABLE `reference` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `title` TEXT NOT NULL,
  `details` LONGTEXT NULL,
  `url` LONGTEXT NULL,
  `date` DATE NULL,
  `typeID` INT NOT NULL,
  `reliability` INT NULL,
  `dateUpdate` DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `I_reference_idx` (`id` ASC),
  CONSTRAINT `FK_referenceIDType` FOREIGN KEY (`typeID`)
		REFERENCES `referenceType` (`id`)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION
) CHARACTER SET utf8mb4;

CREATE TRIGGER TR_reference_dateUpdate_updater
BEFORE UPDATE ON `reference`
    FOR EACH ROW
		SET new.dateUpdate = NOW();

CREATE TABLE `quoteType` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `title` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE (`title`)
) CHARACTER SET utf8mb4;

CREATE TABLE `quote` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `title` TEXT NOT NULL,
  `details` LONGTEXT NULL,
  `typeID` INT NOT NULL,
  `dateUpdate` DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `I_quote_idx` (`id` ASC),
  CONSTRAINT `FK_quoteIDType` FOREIGN KEY (`typeID`)
    REFERENCES `quoteType` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) CHARACTER SET utf8mb4;

CREATE TRIGGER TR_quote_dateUpdate_updater
BEFORE UPDATE ON `quote`
    FOR EACH ROW
		SET new.dateUpdate = NOW();

CREATE TABLE `quoteLinkType` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `title` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE (`title`)
) CHARACTER SET utf8mb4;

CREATE TABLE `quoteLink` (
  `quoteMainID` INT NOT NULL,
  `quoteSupportID` INT NOT NULL,
  `typeID` INT NOT NULL,
  `dateUpdate` DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`quoteMainID`, `quoteSupportID`),
  CONSTRAINT `FK_quoteIDLinkType` FOREIGN KEY (`typeID`)
    REFERENCES `quoteLinkType` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_quoteIDLink_main` FOREIGN KEY (`quoteMainID`)
    REFERENCES `quote` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_quoteIDLink_support` FOREIGN KEY (`quoteSupportID`)
    REFERENCES `quote` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) CHARACTER SET utf8mb4;

CREATE TRIGGER TR_quoteLink_dateUpdate_updater
BEFORE UPDATE ON `quoteLink`
    FOR EACH ROW
		SET new.dateUpdate = NOW();

CREATE TABLE `theme` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `title` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE (`title`)
) CHARACTER SET utf8mb4;

CREATE TABLE `quoteTheme` (
  `themeID` INT NOT NULL,
  `quoteID` INT NOT NULL,
  PRIMARY KEY (`themeID`, `quoteID`),
  CONSTRAINT `FK_quoteID_theme` FOREIGN KEY (`themeID`)
    REFERENCES `theme` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `FK_themequoteID` FOREIGN KEY (`quoteID`)
    REFERENCES `quote` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) CHARACTER SET utf8mb4;

CREATE TABLE `quoteReference` (
  `quoteID` INT NOT NULL,
  `referenceID` INT NOT NULL,
  PRIMARY KEY (`referenceID`, `quoteID`),
  CONSTRAINT `FK_referenceID_quote` FOREIGN KEY (`quoteID`)
    REFERENCES `quote` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_quotereferenceID` FOREIGN KEY (`referenceID`)
    REFERENCES `reference` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) CHARACTER SET utf8mb4;

CREATE TABLE `protagonist` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `type` ENUM('person','company'),
  `name` TEXT NOT NULL,
  `link` TEXT NULL,
  `photo` TEXT NULL,
  `dateUpdate` DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `I_protagonist_idx` (`id` ASC)
) CHARACTER SET utf8mb4;

CREATE TRIGGER TR_protagonist_dateUpdate_updater
BEFORE UPDATE ON `protagonist`
    FOR EACH ROW
		SET new.dateUpdate = NOW();

CREATE TABLE `quoteAuthor` (
  `quoteID` INT NOT NULL,
  `authorID` INT NOT NULL,
  PRIMARY KEY (`authorID`, `quoteID`),
  CONSTRAINT `FK_authorID_quote` FOREIGN KEY (`quoteID`)
    REFERENCES `quote` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `FK_quoteauthorID` FOREIGN KEY (`authorID`)
    REFERENCES `protagonist` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) CHARACTER SET utf8mb4;

CREATE TABLE `referenceAuthor` (
  `referenceID` INT NOT NULL,
  `authorID` INT NOT NULL,
  PRIMARY KEY (`authorID`, `referenceID`),
  CONSTRAINT `FK_authorID_reference` FOREIGN KEY (`referenceID`)
    REFERENCES `reference` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `FK_referenceauthorID` FOREIGN KEY (`authorID`)
    REFERENCES `protagonist` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) CHARACTER SET utf8mb4;

CREATE TABLE `person` (
  `id` INT NOT NULL,
  `surname` TEXT NULL,
  `role` TEXT NULL,
  `dateUpdate` DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `I_person_idx` (`id` ASC),
  CONSTRAINT `FK_id_person_protagonist` FOREIGN KEY (`id`)
    REFERENCES `protagonist` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) CHARACTER SET utf8mb4;

CREATE TRIGGER TR_person_dateUpdate_updater
BEFORE UPDATE ON `person`
    FOR EACH ROW
		SET new.dateUpdate = NOW();

CREATE TABLE `company` (
  `id` INT NOT NULL,
  `siret` TEXT NULL,
  `dateUpdate` DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `I_company_idx` (`id` ASC),
  CONSTRAINT `FK_id_company_protagonist` FOREIGN KEY (`id`)
    REFERENCES `protagonist` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) CHARACTER SET utf8mb4;

CREATE TRIGGER TR_company_dateUpdate_updater
BEFORE UPDATE ON `company`
    FOR EACH ROW
		SET new.dateUpdate = NOW();
