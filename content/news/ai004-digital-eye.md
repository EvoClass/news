---
title: "同一把伞换了个背景，AI 还能认出来吗？"
slug: "ai004-digital-eye"
date: "2026-11-11"
category: "course"
language: "zh_CN"
translation_key: "ai004-digital-eye"
source_language: "zh_CN"
author_name: "EvoClass"
tags: ["AI004", "AI 魔法实验室"]
excerpt: "一张照片进入电脑后，会变成怎样的数据？EvoClass 的 AI004《AI 魔法实验室》从像素和分类出发，带初中生认识生成式 AI、智能体，以及什么时候需要人来核对结果。"
cover_url: "https://raw.githubusercontent.com/EvoClass/news/main/assets/news/ai004-digital-eye-v1.webp"
cover_alt: "一张蓝色雨伞图和一幅由纸片拼成的同款像素雨伞并排放在桌上，一只手正摆放一块蓝色方片。"
draft: false
---

设想你要教一个图像分类模型分辨雨伞和帽子。第一批雨伞照片都拍在雨天，第一批帽子照片都拍在室内。看它对这批训练用的照片做判断时，模型似乎认得很好。换一张照片，把同一把伞摆到室内，它还能认出来吗？

这时值得追问的是，模型究竟学到了伞的形状，还是顺手利用了背景？《AI 魔法实验室》从机器接收到的图像信息讲起，再把同样的追问带到生成内容、智能体行动和人工复核。

## 机器怎样看见一把伞

把伞尖附近的照片放大，你会看到一块块颜色。照片里的蓝色伞面，在常见的 RGB 表示里可以存成一格格数值，每格记录红、绿、蓝三个通道的信息。第 1 课先讲像素和颜色，再介绍计算机视觉怎样从图像里寻找形状和纹理。第 2 课把这些数值组织成张量，并讨论送进模型前为什么要整理数据。[第 1 课《机器的数字之眼》](https://evoclass.ai/student/jMDlWhiMSzS3CdfgIZyKGQ/Lesson%201?content_language=zh_CN) · [第 2 课《数据的基本单元（张量）》](https://evoclass.ai/student/jMDlWhiMSzS3CdfgIZyKGQ/Lesson%202?content_language=zh_CN)

可以用方格纸做个小练习。先画出一把伞，再换一种背景色重画。哪些格子变了？哪些轮廓还保留着？人一眼就能把两张画认成同一类，机器能不能做到，要看它怎样从样本里学习。

## 换一张从未见过的照片

第 3 课从带标签的样本讲起，也讲到了过拟合和泛化。过拟合的模型会过分依赖训练样本里的细节，换一批图片就容易失手。判断模型能不能处理新情况，需要留出它训练时没见过的样本来检查。[第 3 课《分类大师》](https://evoclass.ai/student/jMDlWhiMSzS3CdfgIZyKGQ/Lesson%203?content_language=zh_CN)

回到那把伞，可以先准备室内和室外两种背景下的帽子与雨伞照片，再留出另一组做测试。若发现模型总把室内的伞认成帽子，下一轮就可以检查背景是否在训练样本里和类别绑得太紧。一次认错提供了下一步要查的线索。

## 从辨认图片到生成图片、采取行动

识别一张伞的照片和生成一张新的伞图，是两个不同的任务。第 6 课用扩散模型讲解生成过程，从噪声出发，逐步去噪，形成符合条件的图像。第 7 课则把问题带到行动上。智能体收集环境信息、选择动作并执行，行动之后再观察环境怎样变化。比如按规则走纸上迷宫，每走一步就要重新判断当前位置。[第 6 课《生成艺术与扩散模型》](https://evoclass.ai/student/jMDlWhiMSzS3CdfgIZyKGQ/Lesson%206?content_language=zh_CN) · [第 7 课《智能体的核心循环》](https://evoclass.ai/student/jMDlWhiMSzS3CdfgIZyKGQ/Lesson%207?content_language=zh_CN)

## 在相信结果之前，找一个办法检查

最后一课讨论数据偏见、模型幻觉和人工监督。一个适合带去课堂的问题是，**如果结果错了，我可以用什么来发现？** 对图像分类，可以找一张背景完全不同的照片。对生成的回答，可以回到原资料找证据。对会采取行动的系统，还可以想想哪一步该由人确认。[第 10 课《伦理、偏见与人机共生》](https://evoclass.ai/student/jMDlWhiMSzS3CdfgIZyKGQ/Lesson%2010?content_language=zh_CN)

课程面向初中阶段学习者，也适合想带孩子理解 AI 基本原理的家长和教师。可以从简体中文课件的第一课和随页小题开始，先把一张熟悉的照片拆成像素，再回头想想，下一张该拿什么照片来测试。[进入 AI004《AI 魔法实验室》](https://evoclass.ai/courses/jMDlWhiMSzS3CdfgIZyKGQ?lang=zh_CN)
