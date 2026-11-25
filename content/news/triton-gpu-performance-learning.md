---
title: "代码算对了，为什么 GPU 还是不够快？从 Triton 学会检查性能"
slug: "triton-gpu-performance-learning"
date: "2026-11-25"
category: "course"
language: "zh_CN"
translation_key: "triton-gpu-performance-learning"
source_language: "zh_CN"
author_name: "EvoClass"
tags: ["人工智能", "AI023"]
excerpt: "GPU 程序输出正确，并不等于已经有效使用硬件。EvoClass AI023 从向量加法走向性能测量、Softmax 与矩阵运算，帮助学习者把“想让代码更快”变成可以检验的问题。"
draft: false
cover_url: "https://raw.githubusercontent.com/EvoClass/news/2e808d87b16354d638e99e11a49a67cb74601aa9/assets/news/triton-gpu-performance-learning-v1.webp"
cover_alt: "色块在芯片示意旁通过不同长度的搬运路径连接工作区，表现 GPU 计算与数据移动关系的概念插画。"
---

两个程序给出相同结果，运行时间却不一样。换一组输入，原来占优的版本又可能落后。此时，继续把代码写得更短，未必能解释发生了什么。

需要问得更具体：时间花在计算上，还是花在数据移动上？测到的是 GPU 真正完成工作所需的时间，还是 CPU 发出任务的时间？

EvoClass 的 [AI023《Introduction to Triton Programming: A Practical Tutorial》](https://evoclass.ai/courses/SLGi2-o2TeKoa2xtiBcokA?lang=en) 把这些问题放进一条从简单算子到性能优化的学习路径。课程适合已有 Python、数组或张量操作基础，希望继续理解 GPU 程序的读者。

## 先写一个小算子，把正确性的边界找出来

向量加法看起来很简单：把两个数组对应位置的数相加。然而，分成多个数据块并行处理后，每个程序实例负责哪一段，最后一块有没有越过数组边界，都需要明确。

[第 5 课“Implementing Your First Kernel: Vector Addition”](https://evoclass.ai/student/SLGi2-o2TeKoa2xtiBcokA/Lesson%205?content_language=en) 可以作为实践起点。这里的重点不只是写出加法表达式，还包括理解分块、位置计算和边界处理。

Triton 的 [官方向量加法教程](https://triton-lang.org/main/getting-started/tutorials/01-vector-add.html) 同样把结果校验与性能比较放在基本实现之后。先选定可信的参照结果，再检查自己的实现，是后续优化的前提。

尤其值得尝试一些“不整齐”的输入长度。能够恰好填满数据块的例子运行成功，并不能证明尾部不足一块时也处理正确。

## 然后确认，计时测到的到底是什么

性能实验里，一次很漂亮的数字并不够。

GPU 工作通常异步执行。若只在发出任务前后读取 CPU 时间，可能没有等到设备真正完成计算；首次运行还可能包含编译和准备工作。比较两个版本时，输入规模、数据类型、设备与软件环境也需要对应。

[第 6 课“Performance Foundations: Occupancy and Benchmarking”](https://evoclass.ai/student/SLGi2-o2TeKoa2xtiBcokA/Lesson%206?content_language=en) 将计时协议、吞吐量、数据访问和参数选择放在一起讨论。它把“这次跑得快”转化成更可复查的描述：在什么条件下，怎样测量，结果是否重复出现？

学习时可以保留一份简单记录：输入尺寸、运行环境、正确性检查和测量方法。没有这些条件，速度数字很难被别人理解，也很难指导自己的下一次修改。

## 少做算术之外，还能少搬几次数据

有时，限制性能的环节是数据来回读写。

Softmax 提供了一个具体例子：若把求最大值、减去最大值、指数计算、求和与归一化拆开执行，中间结果可能需要多次写回和重新读取。将适合合并的步骤放进一个算子，有机会减少这些往返。

Triton 的 [官方 Fused Softmax 教程](https://triton-lang.org/main/getting-started/tutorials/02-fused-softmax.html) 用能够放入片上存储的特定矩阵行说明融合的收益，也明确了适用条件。这个例子说明的是一种优化机会，不能推出所有输入、所有设备或所有融合实现都会更快。

AI023 的后续课时延伸到归约、数值稳定性、矩阵乘法与算子融合。读到这里，除了追问“减少了多少次读写”，也应继续检查误差与边界：性能改善不能以悄悄改变计算结果为代价。

## 让每次优化，都回答一个明确的问题

一个适合开始的小实验，是保持输入和环境一致，只改变一个参数或一种数据组织方式。先写下预期，再测量；如果结果相反，就回到瓶颈分析，而不是急着寻找另一个更大的参数。

课程中的分块大小比较、验证与调优内容，可以帮助组织这样的过程。这里没有给出 EvoClass 的实测加速成绩，也不承诺学完后某个模型必然提升多少性能。

当前课程内容为英文。阅读课件与在本机运行 GPU 实验是两件事；实践需要兼容的硬件和软件环境，具体安装要求应以所用 Triton 版本的官方文档为准。

从 [课程概览](https://evoclass.ai/courses/SLGi2-o2TeKoa2xtiBcokA?lang=en) 选择向量加法或性能基础开始，给第一次实验留下可复查的记录。这样，下次看到“更快”时，你就能继续说明：快在哪里，为什么，以及在什么条件下成立。
