---
slideinit: "<section markdown=\"1\" data-background=\"https://yyyu200.github.io/DFTbook/img/slidebackground.png\"><section markdown=\"1\">"
vertical: "</section><section markdown=\"1\">"
horizontal: "</section></section><section markdown=\"1\" data-background=\"https://yyyu200.github.io/DFTbook/img/slidebackground.png\"><section markdown=\"1\">"
layout: post
title: Quantum Espresso的功能清单
author: yyyu200
tags: template
subtitle: 
category: project1
notebookfilename: intro
visualworkflow: true
published: true
theme: beige
trans: cube
---

>把整个化学归结成一些数学方程的基本定律已经完全搞清楚了，唯一的问题是方程太复杂难于求解。需要发展近似实用的求解方法，从而达到不需要太多计算量就可以揭示复杂原子体系的主要特性。 ——Paul Dirac，1929。

## Quantum Espresso的功能清单
### 基态计算
+ 自洽场总能，力，应力，科恩-沈轨道；
+ 可分模守恒赝势，超软赝势（范德堡方法），PAW赝势（投影扩展波）；
+ 多种交换关联泛函：从LDA到广义梯度修正（PW91，PBE，B88-P86，BLYP）到超GGA，精确交换(HF)，杂化泛函(PBE0，B3LYP，HSE)；
+ 范德瓦尔斯修正: Grimme D2和D3, Tkatchenko-Scheffler, XDM (交换空穴偶极矩), 非局域范德瓦尔斯泛函(vdw-DF);
+ Hubbard U (DFT+U);
+ 贝里相位极化;
+ 非共线磁性, 自旋轨道耦合.

### 结构优化，分子动力学，势能面
+ 具有准牛顿BFGS预处理的GDIIS;
+ Damped dynamics;
+ Car-Parrinello分子动力学(CP模块);
+ 玻恩-奥本海默分子动力学(PWscf模块):
+ Nudged Elastic Band (NEB) 方法;
+ Meta-Dynamics, 使用PLUMED插件.

### 电化学与特殊边界条件
+ Effective Screening Medium (ESM) method
+ Environment effects with the Environ plug-in

### 响应性质（密度泛函微扰理论）
+ 任意波矢处的声子频率和本征矢量;
+ 完整的声子色散; 实空间原子间力常数;
+ 平移和旋转声学求和规则;
+ 有效电荷和介电张量；
+ 电-声子作用；
+ 三阶非简谐声子寿命，使用D3Q模块；
+ 红外和非共振拉曼截面；
+ EPR和NMR化学位移，使用QE-GIPAW模块；
+ 二维异质结构声子（参考）。

### 谱学性质
+ K−, L1 and L2,3-edge X-ray Absorption Spectra (XSpectra package);
+ Time-Dependent Density Functional Perturbation Theory (TurboTDDFT package);
+ Electron energy-loss spectroscopy (TurboEELS package);
+ Electronic excitations with Many-Body Perturbation Theory (GWL package);
+ Electronic excitations with Many-Body Perturbation Theory, using the YAMBO package.

### 量子输运
+ Ballistic Transport ( PWCOND package);
+ Coherent Transport from Maximally Localized Wannier Functions, using the WanT code;
+ Maximally-localized Wannier functions and transport properties, using the WANNIER90 code.
+ Kubo-Greenwood electrical conductivity using the KGEC code.

### 软件运行平台要求
几乎各种现有平台(真的！手机和游戏机上也能运行)：大型机(IBM SP和BlueGene, Cray XT, Altix, Nec SX)，工作站 (HP, IBM, SUN, Intel, AMD) ，个人电脑，支持操作系统包括Linux, Windows, Mac OS-X, 32位或64位Intel或AMD处理器的集群，以多种方式连接(吉比特以太网, myrinet, infiniband…). 充分利用数学软件库如Intel CPU适合的MKL，AMD CPU适合的ACML，IBM机器使用的ESSL。支持GPU的版本见下载页。



>War does not decide who is right, only who is **left**.
