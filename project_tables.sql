-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 26, 2020 at 07:03 PM
-- Server version: 5.7.24
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `project_tables`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `name` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `name`, `password`) VALUES
(1, 'prince', '123'),
(3, 'prince1', '123'),
(4, 'PRINCE2', 'PRINCE'),
(5, 'ufoeze', '555');

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `id` int(11) NOT NULL,
  `author` varchar(100) NOT NULL,
  `publisher` varchar(100) NOT NULL,
  `title` varchar(100) NOT NULL,
  `edition` varchar(100) NOT NULL,
  `classification` varchar(100) NOT NULL,
  `ref_no` varchar(100) NOT NULL,
  `price` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `total_books` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`id`, `author`, `publisher`, `title`, `edition`, `classification`, `ref_no`, `price`, `date`, `total_books`) VALUES
(1, 'prince', 'prince', 'vvdvdv', 'vdvdv', 'vdjjg', 'jdfjjdd', '500', '2020-10-10', NULL),
(2, 'prince', 'ogr', 'josh', '74th', 'sciene', '521', '400', '2020-12-07', '0'),
(3, 'Joniehn De', 'cway', 'The man who new Infinite', '2009', 'science', '45678', '540002', '2020-05-02', NULL),
(4, 'prince', 'prince', 'prince', 'prince', 'SOCIAL SCIENCES(300-399)', '123', '200', '2020-11-15', '12'),
(5, 'TRGRT', 'HTRR', 'HTRTR', 'RHRTRHR', 'PHILOSOPHY(100-199)', '122', '300', '2020-11-14', '12');

-- --------------------------------------------------------

--
-- Table structure for table `borrowers_table`
--

CREATE TABLE `borrowers_table` (
  `id` int(11) NOT NULL,
  `title_of_book` varchar(200) NOT NULL,
  `author` varchar(100) NOT NULL,
  `ref_number` varchar(100) NOT NULL,
  `borrowers_name` varchar(100) NOT NULL,
  `reg_no` varchar(100) NOT NULL,
  `date_of_rent` date NOT NULL,
  `date_of_exp` date NOT NULL,
  `book_classification` varchar(255) NOT NULL,
  `book_id` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `borrowers_table`
--

INSERT INTO `borrowers_table` (`id`, `title_of_book`, `author`, `ref_number`, `borrowers_name`, `reg_no`, `date_of_rent`, `date_of_exp`, `book_classification`, `book_id`) VALUES
(1, 'web', 'prince', 'kkhgfc', 'khvb', 'khuyx', '2020-12-31', '2020-05-12', 'ARTS(600-699)', ''),
(2, 'TTTTT', 'yfsxfc', 'yrsedrfg', '6resdrt', 'yfyerdf', '2020-02-02', '2020-08-05', 'SOCIAL SCIENCES(300-399)', ''),
(3, 'web', 'web', 'web', 'web', 'web', '2020-05-06', '2020-05-01', 'PHILOSOPHY(100-199)', ''),
(4, 'web', 'web', 'sjsnndnd', 'ufoeze prince', 'co3/019/2098', '2020-07-26', '2020-12-13', 'ARTS(600-699)', ''),
(5, 'xcrrgd', 'vddgcdxgd', 'WEB', 'web', 'rrrr', '2024-08-11', '2020-06-18', 'LANGUAGE(400-499)', ''),
(6, 'fdfdf', 'kfdg', 'fddffdf', 'dfdfdf', 'fdddf', '2021-11-13', '2025-11-02', 'NATURAL SCIENCE(500-599)', ''),
(7, 'jhjhfm', 'hythy', 'thhtyh', 'iukkiuhh', 'rhrhr', '2020-11-28', '2024-11-29', 'PHILOSOPHY', ''),
(8, 'ABI', 'chinu achebe', 'COD6D', 'prince', 'CO3/019/2098', '2022-11-01', '2030-11-02', 'PHILOSOPHY(100-199)', ''),
(9, 'PRINCE', 'PRINCE', 'PRINCE', 'PRINCE', 'PRINCE', '2020-11-28', '2022-11-06', 'HISTORY(900-999)', ''),
(10, 'josh', 'lhej', 'jyrjty', 'fdghtr', 'fght', '2020-11-22', '2025-11-15', 'GENERAL WORKES(000-099)', NULL),
(11, 'josh', 'dfgv', 'bbtt', 'fv', 'bgb', '2020-11-25', '2020-11-20', 'BOOK CLASSIFICATION', NULL),
(12, 'josh', 'csce', 'fevvfv', 'adfv', 'fvvdf', '2020-11-25', '2020-11-27', 'RELIGION(200-299)', NULL),
(13, 'JOSH', 'KVJK', 'UYGHJK', 'KJHJ', 'LKJTR', '2020-11-26', '2020-11-28', 'BOOK CLASSIFICATION', NULL),
(14, 'JOSH', 'KJHGHJ', 'LKJHFFGHIJ', 'LKU', ',KJHGF', '2032-11-25', '2028-11-12', 'LANGUAGE(400-499)', NULL),
(15, 'JOSH', 'KJHGFGH', 'OIUYGFGH', 'LKJHGHJ', 'LKJHGH', '2052-11-29', '2035-11-30', 'RELIGION(200-299)', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `library_users`
--

CREATE TABLE `library_users` (
  `id` int(11) NOT NULL,
  `user_name` varchar(100) NOT NULL,
  `reg_number` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `telephone` varchar(100) NOT NULL,
  `expiring_date` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `library_users`
--

INSERT INTO `library_users` (`id`, `user_name`, `reg_number`, `address`, `telephone`, `expiring_date`) VALUES
(1, 'web', 'web', 'java', '08033354785', '2020-12-12'),
(2, 'prince', 'ufoeze', 'no 36 HH own esete lagos', '08100069880', '2020-03-02'),
(3, 'prince', 'co3-2098', 'web', 'hoodd', '2020-05-05'),
(4, 'prince', 'ufoeze', '30 gods own estzte', '08100069880', '2020-05-09'),
(5, 'prince', 'ugochukwu', '32gods own estste ', '08100069880', '2020-12-12'),
(6, 'santi', 'co2/015/2098', 'gbfg', '08100069880', '2005-05-01'),
(7, 'josh', 'gfghf', 'ghnghndg', '08100069880', '2001-01-05');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `borrowers_table`
--
ALTER TABLE `borrowers_table`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `library_users`
--
ALTER TABLE `library_users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `borrowers_table`
--
ALTER TABLE `borrowers_table`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `library_users`
--
ALTER TABLE `library_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
