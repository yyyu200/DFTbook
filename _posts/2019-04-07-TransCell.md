---
slideinit: "<section markdown=\"1\" data-background=\"https://yyyu200.github.io/DFTbook/img/slidebackground.png\"><section markdown=\"1\">"
vertical: "</section><section markdown=\"1\">"
horizontal: "</section></section><section markdown=\"1\" data-background=\"https://yyyu200.github.io/DFTbook/img/slidebackground.png\"><section markdown=\"1\">"
layout: post
title: 建立QE的晶体模型
author: yyyu200
tags: DFT
subtitle: 
category: Blogs
notebookfilename: intro
visualworkflow: true
published: true
theme: beige
trans: cube
---

* TOC
{:toc}

先哲卡利马科斯 (Callimachus) 曾经言道：“一部大书是一项大罪”[注1]。就罪过而言，希望我写这本密度泛函计算的书是一本小书。而我今天介绍的这本大书：International Tables for Crystallography（ITC），ITC包括9卷，7000多页，希望如其名，只是一些表格，而被豁免。

首先，我试图说明以下几个概念：

平移群，点群，空间群，晶体，原胞，晶胞，布拉伐格子，晶系，晶面，布里渊区。

**群**，是一种代数结构，在集合上封闭的运算，运算满足结合律，存在单位元，存在逆元，定义为群。

**晶体**，是自然形成和人工合成的固体的形态，大量原子周期性排列则为晶体，由于结合能最低，纯净物在熔融条件下缓慢降温会自发形成晶体。

可以将空间中的晶体坐标看成集合，在考虑块材性质时，可以认为晶体在空间无限延伸，允许其转动、平移，则可以构成群，转动、反演为群的运算，或称之为变换、操作。

如果只允许平移，称为**平移群**。

如果只允许转动（含空间反演、镜像），称为**点群**，3维空间中的点群有32种。

如果允许转动和平移的复合操作，称为**空间群**，3维空间中的空间群有230种。指定了空间群的类型，我们只需要知道在空间群操作下不重复的原子位置，就可以确定晶体结构，这些不重复的位置称为Wyckoff位置，QE输入有space_group和ATOMIC_POSITIONS { crystal_sg }来专门设置。

保持平移对称性的最小单元是**原胞**。

保持平移对称性和点群对称性的最小单元是**晶胞。

按照基元+格子的概念，确定**布拉伐格子**应满足：（1）所选平行六面体必须充分反映出格子的点群与平移群，即平行六面体必须与整个格子的晶系特征一致。（2）所选择平行六面体各个棱之间夹角为直角的数目最多，不为直角者尽可能地接近直角。（3）在满足上述（1）（2）条件后，所选择的平行六面体的体积应为最小。布拉伐格子即为晶胞。3维空间的布拉伐格子有14种。

在平移操作下，晶体保持不变，这种在某种操作下不变的性质称之为体系的对称性。体系的薛定谔方程，由于体系的对称性，具有变换下不变的性质，于是有量子数来标记这些变换，晶体平移对称性是一系列准连续的k值所标记的，k点所在空间称为k空间，k空间是相对晶体的原胞定义的，计算晶体的能带就是在k空间进行的，k空间也具有周期性，取0点周围的魏格纳塞茨原胞，称为第一**布里渊区**。

**晶面**是相对于晶胞定义的。

14种布拉伐格子，按照具有的点群分类，分为7种**晶系**，即：

triclinic, monoclinic, orthorhombic, tetragonal, rhombohedral, hexagonal, and cubic。

其中rhombohedral有两种晶胞表示，一种是菱方，一种是六方，六方体积是菱方的三倍，在QE输入中有专门的设定。


# QE中的结构定义

结构定义有ibrav等于零和ibrav不等于零两种方式。

ibrav不等于零时，这里强烈推荐只用来计算材料的原胞，这时，ibrav的值代表布拉伐格子的类型。

设置ibrav=0，这时需要在输入文件中写入CELL_PARAMETERS，即晶格的基矢量。

# 将晶胞转换为原胞

## 1. 变换的数学形式

注释

1 这句名言的另一种译文是“大书，大恶”，希腊原文则为“μέγα βιβλίον μέγα κακόν”。


## References

1. International Tables for Crystallography (2006). Vol. A, Chapter 5.1, pp. 78–85.

