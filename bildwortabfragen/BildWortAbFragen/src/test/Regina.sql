-- phpMyAdmin SQL Dump
-- version 4.1.7
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Aug 13, 2014 at 05:14 PM
-- Server version: 5.5.35-MariaDB-log
-- PHP Version: 5.5.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `Regina`
--

-- --------------------------------------------------------

--
-- Table structure for table `Local`
--

CREATE TABLE IF NOT EXISTS `Local` (
  `SynthFile` varchar(80) NOT NULL,
  `HandFile` varchar(80) NOT NULL,
  `HandWord` varchar(80) NOT NULL,
  `Score` double NOT NULL,
  `Zoni` varchar(3) NOT NULL,
  `Platos` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='DTW with LGH';

-- --------------------------------------------------------

--
-- Table structure for table `Stiles`
--

CREATE TABLE IF NOT EXISTS `Stiles` (
  `SynthFile` varchar(80) NOT NULL,
  `HandFile` varchar(80) NOT NULL,
  `HandWord` varchar(80) NOT NULL,
  `Score` double NOT NULL,
  `Zoni` varchar(3) NOT NULL,
  `Platos` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='DTW with columns';

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
