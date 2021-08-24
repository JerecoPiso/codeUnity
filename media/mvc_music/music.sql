-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 20, 2020 at 02:19 AM
-- Server version: 10.1.30-MariaDB
-- PHP Version: 7.2.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `music`
--

-- --------------------------------------------------------

--
-- Table structure for table `album`
--

CREATE TABLE `album` (
  `id` int(11) NOT NULL,
  `artist_id` varchar(100) NOT NULL,
  `title` varchar(100) NOT NULL,
  `year` varchar(40) NOT NULL,
  `no_of_songs` varchar(100) NOT NULL,
  `sold` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `album`
--

INSERT INTO `album` (`id`, `artist_id`, `title`, `year`, `no_of_songs`, `sold`) VALUES
(1, '22', 'kamikaze', '2013', '14', 20000000),
(2, '22', 'recovery', '2009', '10', 15000000),
(3, '23', 'sukli', '2016', '9', 40000),
(4, '23', 'MKNM', '2012', '11', 65000),
(5, '24', 'Fearless', '2008', '5', 7000000),
(6, '24', 'Red', '2012', '7', 2000000),
(7, '26', 'Goodbye Lullaby', '2011', '3', 1000000),
(8, '26', 'Avril Lavigne', '2013', '5', 4000000),
(9, '27', 'Purpose', '2015', '4', 5000000),
(10, '27', 'Believe', '2012', '5', 5000000),
(12, '28', 'Alive', '2014', '3', 1000000),
(13, '28', 'Sweet Talker', '2013', '3', 1000000),
(14, '29', 'Lemonade', '2016', '5', 3000000),
(15, '29', '4', '2011', '7', 4000000),
(16, '30', 'Circus', '2008', '5', 3000000),
(17, '30', 'Glory', '2016', '5', 2000000),
(18, '31', 'Thriller', '1982', '7', 33000000),
(19, '31', 'Invincible', '2001', '4', 6000000),
(20, '25', 'Materyal', '2017', '6', 35000),
(22, '25', 'Pati Pato', '2018', '6', 20000),
(25, '22', '45', '345', '345', 345);

-- --------------------------------------------------------

--
-- Table structure for table `artists`
--

CREATE TABLE `artists` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `b_date` varchar(30) DEFAULT NULL,
  `no_of_albums` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `artists`
--

INSERT INTO `artists` (`id`, `name`, `b_date`, `no_of_albums`) VALUES
(22, 'EMINEM', '1212-12-12', '5'),
(23, 'Gloc 9', '10-18-1977', '7'),
(24, 'Taylor Swift', '12-13-1989', '8'),
(25, 'Shanti Dope', '4-15-2001', '2'),
(26, 'Avril Lavigne', '7-27-1984', '2'),
(27, 'Justin Bieber', '3-27-1988', '4'),
(28, 'Jessie J', '3-27-1988', '4'),
(29, 'Beyonce', '9-4-1981', '6'),
(30, 'Britney Spears', '12-2-1981', '7'),
(31, 'Michael Jackson', '8-29-1958', '6'),
(32, '45', '2019-11-07', '435'),
(34, 'steph', '2019-04-05', '345'),
(35, '45345345345', '2019-11-06', '345345'),
(36, 'Joe Mar', '2000-03-25', '2100'),
(38, 'Jereco James Piso', '1999-07-18', '4'),
(39, '345', NULL, '34'),
(40, 'hahaha', NULL, '345');

-- --------------------------------------------------------

--
-- Table structure for table `genre`
--

CREATE TABLE `genre` (
  `id` int(11) NOT NULL,
  `genre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `genre`
--

INSERT INTO `genre` (`id`, `genre`) VALUES
(3, 'pop'),
(4, 'hiphop'),
(5, 'blues'),
(6, 'country music'),
(7, 'heavy metal'),
(9, 'folk music');

-- --------------------------------------------------------

--
-- Table structure for table `music`
--

CREATE TABLE `music` (
  `id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `album_id` varchar(100) DEFAULT NULL,
  `artist_id` varchar(100) DEFAULT NULL,
  `duration` varchar(100) DEFAULT NULL,
  `ratings` int(2) NOT NULL,
  `genre` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `music`
--

INSERT INTO `music` (`id`, `title`, `album_id`, `artist_id`, `duration`, `ratings`, `genre`) VALUES
(10, 'Soory', '10', '27', '3:49 mins', 3, 1),
(11, 'BaNG Bang', '13', '28', '3:59 mins', 8, 5),
(12, 'Masterpiece', '13', '28', '3:19 mins', 2, 5),
(13, 'Wild', '12', '28', '3:10 mins', 3, 5),
(14, 'Boyfriend', '10', '27', '3:01 mins', 4, 1),
(15, 'Right Here', '10', '27', '3:33 mins', 5, 3),
(16, 'Love Youself', '9', '27', '3:41 mins', 9, 3),
(17, 'Let me Go', '8', '26', '3:24 mins', 4, 3),
(18, 'Rock n Roll', '8', '26', '3:44 mins', 4, 3),
(19, 'Smile', '7', '26', '3:14 mins', 5, 3),
(20, '22', '6', '24', '3:36 mins', 8, 3),
(21, 'Red', '6', '24', '3:16 mins', 7, 3),
(22, 'Fifteen', '5', '24', '3:56 mins', 5, 3),
(23, 'Sirena', '4', '23', '4:56 mins', 5, 3),
(24, 'Bakit Hindi', '4', '23', '4:26 mins', 4, 4),
(26, 'Kalye', '3', '23', '3:41 mins', 4, 4),
(27, 'No Love', '2', '22', '3:41 mins', 6, 4),
(28, 'Not Afraid', '2', '22', '4:41 mins', 9, 4),
(29, 'Fall', '1', '22', '3:41 mins', 5, 4),
(30, 'Venom', '1', '22', '3:56 mins', 5, 4),
(36, '435345', '9', '22', 'wqe', 0, 0),
(48, 'Nadarang', '20', '25', '3:00 mins', 9, 4),
(63, 'Materyal', '20', '25', '4:00 mins', 7, 4);

-- --------------------------------------------------------

--
-- Table structure for table `music_tag_relationship`
--

CREATE TABLE `music_tag_relationship` (
  `m_id` int(11) DEFAULT NULL,
  `t_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `music_tag_relationship`
--

INSERT INTO `music_tag_relationship` (`m_id`, `t_id`) VALUES
(24, 1),
(25, 1),
(26, 1),
(27, 1),
(28, 1),
(29, 1),
(30, 1),
(15, 5),
(16, 5),
(17, 5),
(18, 5),
(19, 5),
(20, 5),
(21, 5),
(22, 5),
(2, 4),
(4, 4),
(6, 4),
(8, 4),
(1, 1),
(1, 2),
(3, 3),
(5, 3),
(7, 3),
(9, 3),
(11, 3),
(13, 3);

-- --------------------------------------------------------

--
-- Table structure for table `tags`
--

CREATE TABLE `tags` (
  `id` int(11) NOT NULL,
  `tag` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tags`
--

INSERT INTO `tags` (`id`, `tag`) VALUES
(1, '#iLOVErap'),
(2, '#popCorn'),
(3, '#Bluesssssshhh'),
(4, '#musicccLife'),
(5, '#LiveWithMusic');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `album`
--
ALTER TABLE `album`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `artists`
--
ALTER TABLE `artists`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `genre`
--
ALTER TABLE `genre`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `music`
--
ALTER TABLE `music`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tags`
--
ALTER TABLE `tags`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `album`
--
ALTER TABLE `album`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `artists`
--
ALTER TABLE `artists`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `genre`
--
ALTER TABLE `genre`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `music`
--
ALTER TABLE `music`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=64;

--
-- AUTO_INCREMENT for table `tags`
--
ALTER TABLE `tags`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
