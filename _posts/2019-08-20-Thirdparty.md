---
slideinit: "<section markdown=\"1\" data-background=\"../../../../../img/slidebackground.png\"><section markdown=\"1\">"
vertical: "</section><section markdown=\"1\">"
horizontal: "</section></section><section markdown=\"1\" data-background=\"../../../../../img/slidebackground.png\"><section markdown=\"1\">"
layout: post
title: QE模块小结
author: yyyu200
tags: DFT 使用心得
subtitle: ""
category: Blogs
notebookfilename: intro
visualworkflow: true
published: true
theme: beige
trans: cube
---


* TOC
{:toc}

# QE模块小结

材料电子结构第一性原理计算的核心模块是总能和力的计算。在得到稳定的结构、准确的总能及电荷密度、K-S波函数之后，通过这些量得到材料的物理性质（部分化学性质）往往是研究者更加关心的问题。材料的力学、热学、声学、电学（输运）、磁学、光学性质计算与实验测量的互相参考，一直是材料计算发展的指导方向。

QE官网（[Link](http://www.quantum-espresso.org/project/what-can-qe-do) ）给出了功能的清单（[中文](../../../../2018/05/01/QE-List/)）。QE是一个模块化的软件包，安装目录下有很多.x程序，是来自世界多个课题组开发的第三方功能模块，以下对各个模块用法进行介绍。

## neb.x模块——微动弹性带方法


## 超动力学， 使用PLUMED插件。

## 有效屏蔽介质方法(ESM)

## 环境效应，Environ插件。

## 三阶非简谐声子寿命，使用D3Q模块

## EPR和NMR化学位移，使用QE-GIPAW模块

## K，L1和L2，3吸收边X射线吸收谱(XSpectra模块)

## 含时密度泛函微扰理论(TurboTDDFT模块)

## 电子能量损失谱(TurboEELS模块)

## 多体微扰理论计算电子激发态 (GWL模块)

## 多体微扰理论计算电子激发态，使用YAMBO模块。

## 弹道输运（PWCOND模块）

## 基于最局域化万尼尔函数相干输运，使用WanT模块

## 最局域化万尼尔函数与输运性质，使用WANNIER90

## Kubo-Greenwood电导率，使用KGEC。


