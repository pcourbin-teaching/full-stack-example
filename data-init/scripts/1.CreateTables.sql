use debatsido;
set sql_safe_updates=0;

DROP TABLE IF EXISTS Company;
DROP TABLE IF EXISTS Person;
DROP TABLE IF EXISTS SourceAuthor;
DROP TABLE IF EXISTS QuoteAuthor;
DROP TABLE IF EXISTS Entity;
DROP TABLE IF EXISTS SourceQuote;
DROP TABLE IF EXISTS QuoteTheme;
DROP TABLE IF EXISTS Theme;
DROP TABLE IF EXISTS QuoteLink;
DROP TABLE IF EXISTS QuoteLink_Type;
DROP TABLE IF EXISTS Quote;
DROP TABLE IF EXISTS Quote_Type;
DROP TABLE IF EXISTS Source;
DROP TABLE IF EXISTS Source_Type;

CREATE TABLE `Source_Type` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `title` TEXT NOT NULL,
  PRIMARY KEY (`id`)
) CHARACTER SET utf8mb4;

CREATE TABLE `Source` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `title` TEXT NOT NULL,
  `text` LONGTEXT NULL,
  `url` LONGTEXT NULL,
  `date` DATE NULL,
  `id_type` INT NOT NULL,
  `reliability` INT NULL,
  `date_update` DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `F_source_idx` (`id` ASC),
  CONSTRAINT `id_source_type` FOREIGN KEY (`id_type`)
		REFERENCES `Source_Type` (`id`)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION
) CHARACTER SET utf8mb4;

CREATE TRIGGER source_date_update_updater
BEFORE UPDATE ON `Source`
    FOR EACH ROW
		SET new.date_update = NOW();

CREATE TABLE `Quote_Type` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `title` TEXT NOT NULL,
  PRIMARY KEY (`id`)
) CHARACTER SET utf8mb4;

CREATE TABLE `Quote` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `title` TEXT NOT NULL,
  `text` LONGTEXT NULL,
  `id_type` INT NOT NULL,
  `date_update` DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `F_quote_idx` (`id` ASC),
  CONSTRAINT `id_quote_type` FOREIGN KEY (`id_type`)
    REFERENCES `Quote_Type` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) CHARACTER SET utf8mb4;

CREATE TRIGGER quote_date_update_updater
BEFORE UPDATE ON `Quote`
    FOR EACH ROW
		SET new.date_update = NOW();

CREATE TABLE `QuoteLink_Type` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `title` TEXT NOT NULL,
  PRIMARY KEY (`id`)
) CHARACTER SET utf8mb4;

CREATE TABLE `QuoteLink` (
  `id_quote_main` INT NOT NULL,
  `id_quote_support` INT NOT NULL,
  `id_type` INT NOT NULL,
  `date_update` DATETIME DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT `id_quotelink_type` FOREIGN KEY (`id_type`)
    REFERENCES `QuoteLink_Type` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `id_quotelink_main` FOREIGN KEY (`id_quote_main`)
    REFERENCES `Quote` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `id_quotelink_support` FOREIGN KEY (`id_quote_support`)
    REFERENCES `Quote` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) CHARACTER SET utf8mb4;

CREATE TRIGGER quotelink_date_update_updater
BEFORE UPDATE ON `QuoteLink`
    FOR EACH ROW
		SET new.date_update = NOW();

CREATE TABLE `Theme` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `title` TEXT NOT NULL,
  PRIMARY KEY (`id`)
) CHARACTER SET utf8mb4;

CREATE TABLE `QuoteTheme` (
  `id_theme` INT NOT NULL,
  `id_quote` INT NOT NULL,
  CONSTRAINT `id_quote_theme` FOREIGN KEY (`id_theme`)
    REFERENCES `Theme` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `id_theme_quote` FOREIGN KEY (`id_quote`)
    REFERENCES `Quote` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) CHARACTER SET utf8mb4;

CREATE TABLE `SourceQuote` (
  `id_quote` INT NOT NULL,
  `id_source` INT NOT NULL,
  CONSTRAINT `id_source_quote` FOREIGN KEY (`id_quote`)
    REFERENCES `Quote` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `id_quote_source` FOREIGN KEY (`id_source`)
    REFERENCES `Source` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) CHARACTER SET utf8mb4;

CREATE TABLE `Entity` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `type` ENUM('person','company'),
  `name` TEXT NOT NULL,
  `link` TEXT NULL,
  `photo` TEXT NULL,
  `date_update` DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `F_entity_idx` (`id` ASC)
) CHARACTER SET utf8mb4;

CREATE TRIGGER entity_date_update_updater
BEFORE UPDATE ON `Entity`
    FOR EACH ROW
		SET new.date_update = NOW();

CREATE TABLE `QuoteAuthor` (
  `id_quote` INT NOT NULL,
  `id_author` INT NOT NULL,
  CONSTRAINT `id_author_quote` FOREIGN KEY (`id_quote`)
    REFERENCES `Quote` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `id_quote_author` FOREIGN KEY (`id_author`)
    REFERENCES `Entity` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) CHARACTER SET utf8mb4;

CREATE TABLE `SourceAuthor` (
  `id_source` INT NOT NULL,
  `id_author` INT NOT NULL,
  CONSTRAINT `id_author_source` FOREIGN KEY (`id_source`)
    REFERENCES `Source` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `id_source_author` FOREIGN KEY (`id_author`)
    REFERENCES `Entity` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) CHARACTER SET utf8mb4;

CREATE TABLE `Person` (
  `id` INT NOT NULL,
  `surname` TEXT NULL,
  `role` TEXT NULL,
  `date_update` DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `F_person_idx` (`id` ASC),
  CONSTRAINT `id_person_entity` FOREIGN KEY (`id`)
    REFERENCES `Entity` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) CHARACTER SET utf8mb4;

CREATE TRIGGER person_date_update_updater
BEFORE UPDATE ON `Person`
    FOR EACH ROW
		SET new.date_update = NOW();

CREATE TABLE `Company` (
  `id` INT NOT NULL,
  `SIRET` TEXT NULL,
  `date_update` DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `F_company_idx` (`id` ASC),
  CONSTRAINT `id_company_entity` FOREIGN KEY (`id`)
    REFERENCES `Entity` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) CHARACTER SET utf8mb4;

CREATE TRIGGER company_date_update_updater
BEFORE UPDATE ON `Company`
    FOR EACH ROW
		SET new.date_update = NOW();
