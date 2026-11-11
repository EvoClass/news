---
title: "卡在一道题时，怎样请 AI 只给一条提示？"
slug: "ask-ai-for-a-hint"
date: "2026-11-11"
category: "guide"
language: "zh_CN"
translation_key: "ask-ai-for-a-hint"
source_language: "zh_CN"
author_name: "EvoClass"
tags: ["AI 答疑", "自主学习", "编程练习"]
excerpt: "把题目、自己试过的方法和卡住的位置交给 AI，再请它只提示下一步。以一道 Python 判断题为例，走完从提问到独立复做的过程。"
cover_url: "https://raw.githubusercontent.com/EvoClass/news/5dcaa8436d450ed972e05c3bb21b8a9323344d41/assets/news/ask-ai-for-a-hint-v1.webp"
cover_alt: "学习者把铅笔停在草稿纸上的分支点，一面小红旗标出要先检查的位置。"
draft: true
---

设想你要写一条 Python 条件，只打印尚未读完的书。一条记录里的 `finished` 是布尔值。你写了 `if finished:`，运行后却发现读完的书被打印出来了。这个时候，问一句“代码怎么写”很容易拿到一份完整答案，你仍可能说不清原来那一行为什么会错。

可以把问题缩小到眼前的一步。程序什么时候进入这个分支？这和题目希望的时机有什么关系？

## 把题目、尝试和异常放在同一个问题里

在 EvoClass 的课堂里，如果当前课程和账号提供 AI 答疑入口，可以先停在相关课件页，再打开答疑。页面上下文有助于定位当前内容，问题里仍值得写出具体条件。这道练习可以搭配 AI001 的控制流课时。[AI001 Lesson 2｜控制流与逻辑](https://evoclass.ai/student/sICiBLSeS3G1NXV0hCvvMA/Lesson%202?content_language=en) · [EvoClass 课堂答疑更新](https://evoclass.ai/news/release-ai-companion-202609?lang=zh_CN)

「我要只打印未读完的书。读完时 `finished` 是 `True`，未读完时是 `False`。我用了 `if finished:`，结果打印了读完的书。请先给我一条检查条件的提示，留给我自己改代码。」

这样的提问把题目、已经试过的写法和观察到的结果都摆出来了。换一门学科，也可以沿用这三个部分。

## 把提示变成自己能做的检查

一条合适的提示可以是“分别把 `True` 和 `False` 代入条件，看看哪一种会进入分支”。先别急着问下一句，拿纸写两行。第一行记 `True` 时程序做什么，第二行记 `False` 时程序做什么。再看哪一行符合题目。

如果回答直接给出了代码，可以先把对话收起来，按这两种输入自己推一遍。发现回答里有疑问时，回到课件或运行最小的例子核对。跑通之后，试着说出这次修改改变了哪种输入的结果。

## 换一道小题，看看能不能独立完成

把“打印未读完的书”换成“只显示还没有提交的作业”。这次不用打开上一段对话，先写清 `submitted` 为真或为假时分别表示什么，然后自己写条件，拿一条已提交和一条未提交的记录测试。

下次卡住时，可以先问自己“我已经确定了什么，还差哪一个判断”。请 AI 给一个能验证的动作，做完之后把同样的判断带到下一道题里。
