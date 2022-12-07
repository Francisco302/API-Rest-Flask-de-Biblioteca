-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 25-11-2022 a las 11:00:07
-- Versión del servidor: 5.7.36
-- Versión de PHP: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `basebiblioteca`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `autor`
--

DROP TABLE IF EXISTS `autor`;
CREATE TABLE IF NOT EXISTS `autor` (
  `IDAUTOR` int(11) NOT NULL AUTO_INCREMENT,
  `CODIGOAUTOR` varchar(16) DEFAULT NULL,
  `NOMBREAUTOR` varchar(32) DEFAULT NULL,
  `APELLIDOAUTOR` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`IDAUTOR`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `autor`
--

INSERT INTO `autor` (`IDAUTOR`, `CODIGOAUTOR`, `NOMBREAUTOR`, `APELLIDOAUTOR`) VALUES
(1, '111', 'Francisco', 'Sanchez'),
(2, '222', 'Homero', 'De Grecia');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalleprestamo`
--

DROP TABLE IF EXISTS `detalleprestamo`;
CREATE TABLE IF NOT EXISTS `detalleprestamo` (
  `IDDETALLEP` int(11) NOT NULL AUTO_INCREMENT,
  `IDLIBRO` int(11) DEFAULT NULL,
  `IDPRESTAMO` int(11) DEFAULT NULL,
  `CANTIDADDETALLEP` int(11) DEFAULT NULL,
  `FECHAENTREGADETALLEP` date DEFAULT NULL,
  PRIMARY KEY (`IDDETALLEP`),
  KEY `FK_ESTA` (`IDLIBRO`),
  KEY `FK_TIENE` (`IDPRESTAMO`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libro`
--

DROP TABLE IF EXISTS `libro`;
CREATE TABLE IF NOT EXISTS `libro` (
  `IDLIBRO` int(11) NOT NULL AUTO_INCREMENT,
  `IDAUTOR` int(11) NOT NULL,
  `ISBNLIBRO` varchar(16) DEFAULT NULL,
  `TITULOLIBRO` varchar(128) DEFAULT NULL,
  `VALORPRESTAMOLIBRO` decimal(8,2) DEFAULT NULL,
  PRIMARY KEY (`IDLIBRO`),
  KEY `FK_ESCRIBE` (`IDAUTOR`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `libro`
--

INSERT INTO `libro` (`IDLIBRO`, `IDAUTOR`, `ISBNLIBRO`, `TITULOLIBRO`, `VALORPRESTAMOLIBRO`) VALUES
(1, 1, '111', 'Primer libro', NULL),
(2, 2, '222', 'La Odisea', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prestamo`
--

DROP TABLE IF EXISTS `prestamo`;
CREATE TABLE IF NOT EXISTS `prestamo` (
  `IDPRESTAMO` int(11) NOT NULL AUTO_INCREMENT,
  `NUMEROPRESTAMO` int(11) DEFAULT NULL,
  `FECHAPRESTAMO` date DEFAULT NULL,
  `DESCRIPCIONPRESTAMO` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`IDPRESTAMO`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
