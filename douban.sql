/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50559
Source Host           : localhost:3306
Source Database       : douban

Target Server Type    : MYSQL
Target Server Version : 50559
File Encoding         : 65001

Date: 2018-03-16 18:34:08
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
) ENGINE=InnoDB AUTO_INCREMENT=159 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of douban
-- ----------------------------
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
INSERT INTO `douban` VALUES ('118', '犯罪', '27');
INSERT INTO `douban` VALUES ('119', '剧情', '219');
INSERT INTO `douban` VALUES ('120', '爱情', '77');
INSERT INTO `douban` VALUES ('121', '同性', '2');
INSERT INTO `douban` VALUES ('122', '动作', '17');
INSERT INTO `douban` VALUES ('123', '喜剧', '44');
INSERT INTO `douban` VALUES ('124', '战争', '28');
INSERT INTO `douban` VALUES ('125', '动画', '27');
INSERT INTO `douban` VALUES ('126', '奇幻', '37');
INSERT INTO `douban` VALUES ('127', '灾难', '7');
INSERT INTO `douban` VALUES ('128', '历史', '20');
INSERT INTO `douban` VALUES ('129', '科幻', '42');
INSERT INTO `douban` VALUES ('130', '悬疑', '26');
INSERT INTO `douban` VALUES ('131', '冒险', '50');
INSERT INTO `douban` VALUES ('132', '音乐', '20');
INSERT INTO `douban` VALUES ('133', '歌舞', '10');
INSERT INTO `douban` VALUES ('134', '儿童', '10');
INSERT INTO `douban` VALUES ('135', '家庭', '22');
INSERT INTO `douban` VALUES ('136', '传记', '10');
INSERT INTO `douban` VALUES ('137', '惊悚', '10');
INSERT INTO `douban` VALUES ('138', '犯罪', '62');
INSERT INTO `douban` VALUES ('139', '剧情', '429');
INSERT INTO `douban` VALUES ('140', '爱情', '133');
INSERT INTO `douban` VALUES ('141', '同性', '2');
INSERT INTO `douban` VALUES ('142', '动作', '47');
INSERT INTO `douban` VALUES ('143', '喜剧', '110');
INSERT INTO `douban` VALUES ('144', '战争', '48');
INSERT INTO `douban` VALUES ('145', '动画', '60');
INSERT INTO `douban` VALUES ('146', '奇幻', '89');
INSERT INTO `douban` VALUES ('147', '灾难', '7');
INSERT INTO `douban` VALUES ('148', '历史', '40');
INSERT INTO `douban` VALUES ('149', '科幻', '68');
INSERT INTO `douban` VALUES ('150', '悬疑', '55');
INSERT INTO `douban` VALUES ('151', '冒险', '119');
INSERT INTO `douban` VALUES ('152', '音乐', '25');
INSERT INTO `douban` VALUES ('153', '歌舞', '12');
INSERT INTO `douban` VALUES ('154', '儿童', '18');
INSERT INTO `douban` VALUES ('155', '家庭', '50');
INSERT INTO `douban` VALUES ('156', '传记', '20');
INSERT INTO `douban` VALUES ('157', '惊悚', '30');
INSERT INTO `douban` VALUES ('158', '纪录片', '1');
