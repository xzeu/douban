/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50559
Source Host           : localhost:3306
Source Database       : douban

Target Server Type    : MYSQL
Target Server Version : 50559
File Encoding         : 65001

Date: 2018-03-16 18:12:13
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for douban
-- ----------------------------
DROP TABLE IF EXISTS `douban`;
CREATE TABLE `douban` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `类别` varchar(255) DEFAULT NULL,
  `数量` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=118 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of douban
-- ----------------------------
INSERT INTO `douban` VALUES ('78', '犯罪', '27');
INSERT INTO `douban` VALUES ('79', '剧情', '219');
INSERT INTO `douban` VALUES ('80', '爱情', '77');
INSERT INTO `douban` VALUES ('81', '同性', '2');
INSERT INTO `douban` VALUES ('82', '动作', '17');
INSERT INTO `douban` VALUES ('83', '喜剧', '44');
INSERT INTO `douban` VALUES ('84', '战争', '28');
INSERT INTO `douban` VALUES ('85', '动画', '27');
INSERT INTO `douban` VALUES ('86', '奇幻', '37');
INSERT INTO `douban` VALUES ('87', '灾难', '7');
INSERT INTO `douban` VALUES ('88', '历史', '20');
INSERT INTO `douban` VALUES ('89', '科幻', '42');
INSERT INTO `douban` VALUES ('90', '悬疑', '26');
INSERT INTO `douban` VALUES ('91', '冒险', '50');
INSERT INTO `douban` VALUES ('92', '音乐', '20');
INSERT INTO `douban` VALUES ('93', '歌舞', '10');
INSERT INTO `douban` VALUES ('94', '儿童', '10');
INSERT INTO `douban` VALUES ('95', '家庭', '22');
INSERT INTO `douban` VALUES ('96', '传记', '10');
INSERT INTO `douban` VALUES ('97', '惊悚', '10');
INSERT INTO `douban` VALUES ('98', '犯罪', '27');
INSERT INTO `douban` VALUES ('99', '剧情', '219');
INSERT INTO `douban` VALUES ('100', '爱情', '77');
INSERT INTO `douban` VALUES ('101', '同性', '2');
INSERT INTO `douban` VALUES ('102', '动作', '17');
INSERT INTO `douban` VALUES ('103', '喜剧', '44');
INSERT INTO `douban` VALUES ('104', '战争', '28');
INSERT INTO `douban` VALUES ('105', '动画', '27');
INSERT INTO `douban` VALUES ('106', '奇幻', '37');
INSERT INTO `douban` VALUES ('107', '灾难', '7');
INSERT INTO `douban` VALUES ('108', '历史', '20');
INSERT INTO `douban` VALUES ('109', '科幻', '42');
INSERT INTO `douban` VALUES ('110', '悬疑', '26');
INSERT INTO `douban` VALUES ('111', '冒险', '50');
INSERT INTO `douban` VALUES ('112', '音乐', '20');
INSERT INTO `douban` VALUES ('113', '歌舞', '10');
INSERT INTO `douban` VALUES ('114', '儿童', '10');
INSERT INTO `douban` VALUES ('115', '家庭', '22');
INSERT INTO `douban` VALUES ('116', '传记', '10');
INSERT INTO `douban` VALUES ('117', '惊悚', '10');
