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

# 谱函数，强关联电子

## K，L1和L2，3吸收边X射线吸收谱(XSpectra模块)

## 含时密度泛函微扰理论(TurboTDDFT模块)

## 电子能量损失谱(TurboEELS模块)

## 多体微扰理论计算电子激发态 (GWL模块)

## 多体微扰理论计算电子激发态，使用YAMBO模块。

## BerkeleyGW: Many-Body Perturbation Theory

https://berkeleygw.org/

## SternheimerGW 

The SternheimerGW code evaluates the quasi-particle correction to the DFT
results in the GW approximation. The Greens function G and the screened
Coulomb W interaction are evaluated solving Sternheimer equations (linear
response problem) instead of summing over the virtual, unoccupied subspace.

The main target of SternheimerGW are very accurate calculations for crystals
and surfaces. We can evaluate the full band structure along any user selected
k-point path. In addition to the quasi-particle corrections to the
eigenvalues, we provide the full frequency dependent spectral function,
which can be compared to angular-resolved photo-emission spectroscopy (ARPES)
experiments.

[1] https://doi.org/10.5281/zenodo.884071

## WEST: Electronic excitations with Many-Body Perturbation Theory

http://www.west-code.org/

WEST is an open source software (released under GPLv3) that performs large-scale, many-body perturbation theory calculations providing electronic and optical spectroscopic characterization of complex materials.

Features:

GW self-energy calculation

Solution of the Bethe Salpeter Equation (BSE) (under development)

Calculation of finite temperature effects (under development)


## QMCPACK: Quantum Monte Carlo calculations

## AMULET: Dynamical Mean Field Theory calculations

# 声子及电声耦合、超导相关

## 三阶非简谐声子寿命，使用D3Q模块

## thermo_pw

https://github.com/dalcorso/thermo_pw

## phono3py

https://atztogo.github.io/phono3py/

## phononpy: Phonon calculation using the Frozen-Phonon approach
http://atztogo.github.io/phonopy/

## PHON: Phonon calculation using the Frozen-Phonon approach
http://www.homepages.ucl.ac.uk/~ucfbdxa/phon/

## ALAMODE: lattice anharmonicity and lattice thermal conductivity of solids

https://alamode.readthedocs.io/en/latest/index.html

## EPW

EPW is the short name for "Electron-phonon Wannier". EPW is an open-source F90/MPI code which calculates properties related to the electron-phonon interaction using Density-Functional Perturbation Theory and Maximally Localized Wannier Functions. EPW is developed and maintained by Samuel Poncé, Roxana Margine, Carla Verdi, and Feliciano Giustino.

Please also consider citing the EPW papers:
1) F. Giustino, M. L. Cohen, and S. G. Louie, Phys. Rev. B 76, 165108 (2007)
2) S. Ponc&rsquo;e, E. R. Margine, C. Verdi and F. Giustino, Comput. Phys. Commun. 209, 116 (2016)

# 输运

## 弹道输运（PWCOND模块）

## 基于最局域化万尼尔函数相干输运，使用WanT模块

## 最局域化万尼尔函数与输运性质，使用WANNIER90

## Kubo-Greenwood电导率，使用KGEC。

## BoltzTraP: Calculation of transport properties

https://www.imc.tuwien.ac.at//forschungsbereich_theoretische_chemie/forschungsgruppen/prof_dr_gkh_madsen_theoretical_materials_chemistry/boltztrap/

# 力学

## ElaStic: Elastic Constants

http://exciting-code.org/elastic

# 结构搜索，高通量计算

## XtalOpt: Evolutionary/Genetic Algorithm

## USPEX: Evolutionary/Genetic Algorithm

## CALYPSO: Crystal structure prediction via Particle Swarm Optimization

## AiiDA: Automated Interactive Infrastructure and Database for Computational Science

# 其他

## neb.x模块——微动弹性带方法

在化学反应、固体的原子扩散中连接初末态最小能量路径（MEP）上的能量最高点称为过渡态（TS）。通常的原子运动用经典力学已经足以描述，分子动力学方法更适合原子振动，过渡态的势垒典型在0.1~1eV量级，如果使用分子动力学，则会出现“罕见现象”（rare event）的问题。同时，可以使用统计方法准确得到转变几率，称为过渡态理论[1]，在玻恩·奥本海默近似的基础上，有两条基本假设，（1）转变几率足够小，反应物符合玻尔兹曼分布。（2）存在维度为D-1的分割表面，从初态到末态的反应只经过分割表面一次，D是系统自由度。由初末状态原子坐标线性插值得到初始的试探解，通过总能梯度和力计算，得到优化反应路径的优化迭代，直至找到TS。

1. Henkelman, G. et al, Journal of Chemical Physics, 113, 9901(2000).

2. H. Jónsson, G. Mills, and K.W. Jacobsen. Classical and Quantum Dynamics in Condensed Phase Simulations Pt. II, Chapter 16: Nudged elastic band method for finding minimum energy paths of transitions.

## 超动力学， 使用PLUMED插件。

## 有效屏蔽介质方法(ESM)

## 环境效应，Environ插件。

## EPR和NMR化学位移，使用QE-GIPAW模块

## NanoTCAD ViDES: Simulation of nanostructured devices

## LOBSTER: a local-orbital basis-set suite for extracting chemical information from plane-wave calculations

## CRITIC2: Bader analysis, laplacian of density and potentials, non-covalent interaction plots and much more

## ATAT 

Thermodynamic modeling of alloys (order-disorder transition, phonons, special quasirandom structures, CALPHAD models, etc.).


# 可视化工具

## Materials Cloud tools

Quantum ESPRESSO input generator and visualizer;
k-point path generator;
phonon visualizer

## PWGui

Input data can be prepared using the graphical user interface PWGui, by Anton Kokalj

## BURAI

An alternative graphical user interface (also for WIndows and Mac): BURAI by Satomichi Nishihara (Version 1.3 available here)

## Schrodinger Materials Science Suite

## Other QE resources found in external sites:

Visualization of the results can be obtained using XCrySDen

Other visualization software that can produce input data or read output data for Quantum ESPRESSO:

VMD, VESTA, GDIS, J-ICE (on-line converter available at this link)

Virtual NanoLab (VNL) graphical user interface, a free product by QuantumWise

NanoHub

