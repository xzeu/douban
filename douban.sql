/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50559
Source Host           : localhost:3306
Source Database       : douban

Target Server Type    : MYSQL
Target Server Version : 50559
File Encoding         : 65001

Date: 2018-03-16 18:45:53
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
) ENGINE=InnoDB AUTO_INCREMENT=180 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of douban
-- ----------------------------
INSERT INTO `douban` VALUES ('159', '犯罪', '62');
INSERT INTO `douban` VALUES ('160', '剧情', '429');
INSERT INTO `douban` VALUES ('161', '爱情', '133');
INSERT INTO `douban` VALUES ('162', '同性', '2');
INSERT INTO `douban` VALUES ('163', '动作', '47');
INSERT INTO `douban` VALUES ('164', '喜剧', '110');
INSERT INTO `douban` VALUES ('165', '战争', '48');
INSERT INTO `douban` VALUES ('166', '动画', '60');
INSERT INTO `douban` VALUES ('167', '奇幻', '89');
INSERT INTO `douban` VALUES ('168', '灾难', '7');
INSERT INTO `douban` VALUES ('169', '历史', '40');
INSERT INTO `douban` VALUES ('170', '科幻', '68');
INSERT INTO `douban` VALUES ('171', '悬疑', '55');
INSERT INTO `douban` VALUES ('172', '冒险', '119');
INSERT INTO `douban` VALUES ('173', '音乐', '25');
INSERT INTO `douban` VALUES ('174', '歌舞', '12');
INSERT INTO `douban` VALUES ('175', '儿童', '18');
INSERT INTO `douban` VALUES ('176', '家庭', '50');
INSERT INTO `douban` VALUES ('177', '传记', '20');
INSERT INTO `douban` VALUES ('178', '惊悚', '30');
INSERT INTO `douban` VALUES ('179', '纪录片', '1');
