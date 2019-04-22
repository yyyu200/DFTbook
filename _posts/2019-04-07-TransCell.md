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

>建模型的第一原理是要符合实际。

* TOC
{:toc}

# 晶体结构

首先，说明以下几个概念：平移群，点群，空间群，原胞，晶胞，布拉伐格子，晶系，晶面，布里渊区。

**晶体**，是自然形成和人工合成的固体的形态，大量原子周期性排列则为晶体，由于结合能最低，纯净物在熔融条件下缓慢降温会自发形成晶体。

**群**，是一种代数结构，在集合上封闭的运算，运算满足结合律，存在单位元，存在逆元，定义为群。可以将空间中的晶体坐标看成集合，在考虑块材性质时，可以认为晶体在空间无限延伸，允许其转动、平移，则可以构成群，转动、反演为群的运算，或称之为变换、操作。

如果只允许平移，称为**平移群**。

如果只允许转动（含空间反演、镜像），称为**点群**，3维空间中的点群有32种。

如果允许转动和平移的复合操作，称为**空间群**，3维空间中的空间群有230种。指定了空间群的类型，我们只需要知道在空间群操作下不重复的原子位置，就可以确定晶体结构，这些不重复的位置称为Wyckoff位置，QE输入有space_group和ATOMIC_POSITIONS { crystal_sg }来专门设置。

保持平移对称性的最小单元是**原胞**。

保持平移对称性和点群对称性的最小单元是**晶胞**。

**布拉伐格子**是按照基元+格子的概念定义的，确定布拉伐格子应满足：（1）所选平行六面体必须充分反映出格子的点群与平移群，即平行六面体必须与整个格子的晶系特征一致。（2）所选择平行六面体各个棱之间夹角为直角的数目最多，不为直角者尽可能地接近直角。（3）在满足上述（1）（2）条件后，所选择的平行六面体的体积应为最小。布拉伐格子即为晶胞。3维空间的布拉伐格子有14种。[下图](https://en.wikipedia.org/wiki/Bravais_lattice)是14种布拉伐格子的基矢a,b,c及夹角$\alpha, \beta, \gamma$所具有的特定关系。

<p align="center">
    <img src="https://yyyu200.github.io/DFTbook/img/BravaisLattices.png" width="563" />
</p>

在特定的平移、旋转操作下，晶体保持不变，这种在某种操作下不变的性质称之为体系的对称性，不同的操作定义了不同的对称性，例如，沿$\vec a$方向平移2个平移基矢等。体系的薛定谔方程，由于体系的对称性，也具有变换下不变的性质，于是有量子数来标记这些变换，晶体平移对称性是一系列准连续的k值所标记的，k点所在空间称为k空间，k空间是相对晶体的原胞定义的，计算晶体的能带就是在k空间进行的，k空间也具有周期性，取原点周围的魏格纳-塞茨原胞，称为第一**布里渊区**。

**晶面**是相对于晶胞定义的。

14种布拉伐格子，按照具有的点群分类，分为7种**晶系**（crystal system），即：

triclinic, monoclinic, orthorhombic, tetragonal, trigonal, hexagonal和cubic。

# QE中的结构定义

QE输入文件的总体结构如下图，输入文件的前半部分满足Fortran语言的Namelist语法。与结构有关的包括```SYSTEM```部分的```ibrav,celldm,nat,ntyp```以及```ATOMIC_POSITIONS```和```CELL_PARAMETERS```共三个部分。

<p align="center">
    <img src="https://yyyu200.github.io/DFTbook/img/structure_input.png" width="503" />
</p>

QE计算的结构都是在三维空间中周期性重复的，所以需要定义一个周期性的单元（这里称作CELL，单元），一般是一个平行六面体的三个基矢量，另外需要定义周期性单元内的原子坐标。QE中的结构定义首先确定了CELL，在QE中用三个矢量$\vec{v_{1}},\vec{v_{2}},\vec{v_{3}}$定义CELL。CELL的定义不依赖于**空间直角坐标系**（**笛卡尔坐标系**）的选择，只需要定义三个基矢量的长度和三个夹角，但是为了计算，需要确定一个空间直角坐标系，以写出各个矢量的笛卡尔坐标，

$$\vec{v_{1}}=(v_{11},v_{12},v_{13}),\vec{v_{2}}=(v_{21},v_{22},v_{23}),\vec{v_{3}}=(v_{31},v_{32},v_{33})$$，

这里空间直角坐标系的选取，对于```ibrav```$\neq$0是在QE程序内部进行的，对于```ibrav=0```是用户通过CELL_PARAMETERS而确定的。

设置```ibrav=0```，这时需要在输入文件中写入```CELL_PARAMETERS```，即CELL的基矢量$\vec{v_{1}},\vec{v_{2}},\vec{v_{3}}$，基矢量是空间直角坐标系中的直角坐标（笛卡尔坐标），空间直角坐标系的选法有一定的任意性，用户可以根据习惯选择，比如，将原点放在某个原子上，将z轴定义为布拉伐格子的基矢c方向，这里坐标系的不同选择，对应的原子坐标会有一个单位正交矩阵所定义的变换，但是要求是右手系。坐标的单位有三种选择：alat，bohr，angstrom，其中，alat是由```celldm(1)```或```A```定义的晶格常数单位。设置```ibrav=0```并写出```CELL_PARAMETERS```这种方法适合用来设置超胞、slab模型等，也可以用来建原胞，是一种通用性较好的方法，并且与其他结构文件格式转换较为方便，也更方便进行后续计算。

设置```ibrav```$\neq$0，这时会生成布拉伐格子相应的原胞。[表1](#tab1)列出了```ibrav```和```celldm```设置以及对应的$\vec{v_{1}},\vec{v_{2}},\vec{v_{3}}$原胞基矢量（相当于内部生成的```CELL_PARAMETERS```），注意```celldm(1)```定义了alat，单位只能是Bohr；```celldm(2)```和```celldm(3)```定义的是比例b/a和c/a，而不是基矢长度，```celldm(4:6)```是角度的余弦值；对于```ibrav=5,-5,9,-9,12,-12```分别是三方、底心正交、简单单斜原胞的两种空间直角坐标系的取法；```ibrav```$\neq$0也可以用来设置超胞等结构，但是超胞推荐```ibrav=0```的方法。[注1](#note1) [注2](#note2)

在QE中还可以直接给出晶格的基矢长度和夹角```A, B, C, cosAB, cosAC, cosBC```，单位是Angstrom，和celldm一样，唯一地确定了CELL，定义了$\vec{v_{1}},\vec{v_{2}},\vec{v_{3}}$，这时的空间直角坐标系是QE内部定义的，也由表1给出。

<span id = "tab1"><center><b>表1</b> 14种布拉伐格子的设置及对应的单元基矢量</center></span>

<p align="center">
    <img src="https://yyyu200.github.io/DFTbook/img/ibrav.png" width="830" />
</p>

在定义了CELL之后，用```ATOMIC_POSITIONS```定义CELL中原子的坐标。```ATOMIC_POSITIONS```的单位有以下可供选择\{ alat \| bohr \| angstrom \| crystal \| crystal_sg \}，其中，crystal是指以$\vec{v_{1}},\vec{v_{2}},\vec{v_{3}}$为基矢量的分数坐标，$\vec{X}=(x_{1},x_{2},x_{3})=x_{1}\vec{v_{1}}+x_{2}\vec{v_{2}}+x_{3}\vec{v_{3}}$。如果选择\{ alat \| bohr \| angstrom\}，则原子坐标是空间直角坐标，由于结构的周期性，这里的空间直角坐标系的选择是任意的，但是习惯上还是与CELL的空间直角坐标系保持一致，坐标值在CELL_PARAMTERS所定义的平行六面体内部。\{crystal_sg\}是在指定了空间群之后，定义对称性不等价的原子位置，与```space_group, uniqueb, origin_choice, rhombohedral```配套使用。

QE提供多种方式完成一件任务的设计风格，为具有各种习惯的用户提供了得心应手的工具，但是对于初学者来说，难免有一种眼花缭乱的感觉，这里推荐一种通用的方法定义CELL，即设置```ibrav=0```，```celldm(1)```= 1 / 0.52917720859 = 1.88972613289 ，于是将alat设置成 1.88972613289 Bohr=1.0 Angstrom （1 Bohr = 0.52917720859 Angstrom），同时显式地写出以Angstrom为单位的```CELL_PARAMETERS {alat}```，这种设置对后续处理电荷文件也提供了方便。对于```ATOMIC_POSITIONS```建议使用分数坐标，即写成```ATOMIC_POSITIONS {crystal}```，分数坐标的三个分量值建议保持在0到1之间，更符合习惯。

最后，强烈建议做好结构之后，用可视化的软件如VESTA、Xcrysden、MS等画出晶体结构，检查一下原子间距等是否正确，这些软件并不都支持QE的输入格式，可能需要转换格式，这时用ibrav=0也比较有利。

# 晶胞和原胞的相互转换

首先，定义一般的周期性单元CELL的变换。按照文献[1]的约定，将（分数）坐标写为列矢量，基矢量$\vec{a},\vec{b},\vec{c}$也各为列矢量。点X在基矢$O,\vec{a},\vec{b},\vec{c}$（$O$为原点）下的坐标$x_{1},x_{2},x_{3}$定义为
$$\vec{X}=x_{1}\vec{a}+x_{2}\vec{b}+x_{3}\vec{c}
=(\vec{a},\vec{b},\vec{c})\quad
\begin{pmatrix}
x_{1} \\x_{2} \\x_{3}
\end{pmatrix}
\quad$$。

考虑晶格静止不动，选择不同的基矢，即选取不同的CELL，同一个点X对新的基矢$O',\vec{a'},\vec{b'},\vec{c'}$有坐标
$$\vec{X'}=x'_{1}\vec{a'}+x'_{2}\vec{b'}+x'_{3}\vec{c'}$$。本节考虑有撇号和无撇号的基矢选择下基矢和坐标的变换关系。

周期性单元CELL的变换是一种特殊的仿射变换（数学上一般的仿射变换形成的新单元并不保证具有晶格周期性），可以分解为线性部分和平移两个部分。

线性部分包括基矢方向和长度的改变，由一个矩阵$\mathbf{P}$表示。$$(\vec{a'},\vec{b'},\vec{c'})=(\vec{a},\vec{b},\vec{c})\mathbf{P}=(\vec{a},\vec{b},\vec{c})\quad
\begin{pmatrix}
P_{11}& P_{12} &P_{13} \\
P_{21}& P_{22} &P_{23} \\
P_{31}& P_{32} &P_{33} \\
\end{pmatrix}
\quad\\
=(P_{11}\vec{a}+P_{21}\vec{b}+P_{31}\vec{c},
P_{12}\vec{a}+P_{22}\vec{b}+P_{32}\vec{c},
P_{13}\vec{a}+P_{23}\vec{b}+P_{33}\vec{c}
) $$。

知道了矩阵$\mathbf{P}$和逆矩阵$\mathbf{Q}=\mathbf{P}^{-1}$，就可以进行CELL之间的变换，常见的晶胞转换为原胞的变换矩阵由表2给出，反之交换$\mathbf{P}$和$\mathbf{Q}$得到。

<p align="center">
    <img src="https://yyyu200.github.io/DFTbook/img/trans_cell.png" width="830" />
</p>

周期性单元CELL的变换，还可以包含平移，平移$\vec{p}$用变换前的基矢定义为：$\vec{p}=p_{1}\vec{a}+p_{2}\vec{b}+p_{3}\vec{c}$。平移的逆变换$\vec{q}=q_{1}\vec{a'}+q_{2}\vec{b'}+q_{3}\vec{c'}$，有$\vec{q}=-\mathbf{P}^{-1}\vec{p}$。

分数坐标的变换公式为：
$\quad
\begin{pmatrix} 
x^\prime_{1} \\ 
x^\prime_{2} \\ 
x^\prime_{3}
\end{pmatrix} \quad=\mathbf{Q}\quad \begin{pmatrix} 
x_{1} \\ 
x_{2} \\ 
x_{3} 
\end{pmatrix} \quad+\vec{q}
$

以体心立方W、Pt3O4，面心立方NaCl，底心$\alpha-$FeSe为例，用[TransCell](https://github.com/yyyu200/SlabMaker)变换CELL和原子坐标，并用VESTA验证（待续）。

# 分数坐标和直角坐标的相互转换


# 非周期性系统

分子、团簇、纳米晶体、具有点缺陷的固体等不具有周期性，纳米线是1维周期性的，固体表面、量子阱、二维材料等是2维周期性的，QE这样的基于平面波基函数的程序，对于这些非三维周期性的材料需要采取**超胞**近似，选取足够大的周期单元，并且，需要时在CELL中的一部分空间不加入任何原子，也就是引入真空，以隔离非周期性的维度。

# 平板（slab）模型的建立

<p align="center">
    <img src="https://kitchingroup.cheme.cmu.edu/dft-book/images/surface-construction.png" width="300" />
</p>

对于固体表面，平面波计算要首先建立平板模型，选取垂直晶面方向足够厚的平板，并且加入足够厚的真空，以消除表面之间的作用，实现表面性质的计算。对于异质结构，如超晶格，需要建立repeated-slab模型，二维材料异质结，如双层石墨烯“魔角”，模型建立也会遇到有共性的问题。

对于有重构（也叫再构，reconstruction，是指表面原子发生面内平移对称性的变化）的晶体表面，要按照重构截取面内的单元，重构原子的坐标要按照实验结构或经验手动设置，这是因为如果初始位置与要研究的重构表面如果相差较大，及时原子个数相同，弛豫的结果也可能是某个亚稳态结构，所以通过relax不能保证弛豫到要研究的特定重构表面结构。

对于没有重构的晶体表面，需要考虑如下：

首先，确定要计算的晶面。晶面用密勒指数标记，密勒指数是不过原点的平面在基矢方向的截距倒数约化成的整数比，注意密勒指数是相对晶胞定义的，通常是三个数，如(001)，(110), (531)等等，一般低密勒指数的面较常见，但实验上也会出现高密勒指数的面。对于六方和三方（菱方）晶体，习惯上用四个数的密勒指数，如(0001),(1-101)等，这里是选了垂直三重旋转轴的面内3个基矢以及沿着三重旋转轴的1个基矢，一共4个基矢而定义的密勒指数，其中，前三个指数的和一定是零，所以只有3个独立的指数，有的文献对于六方或三方结构的晶面也用三指数的表示。晶面确定后，还要根据实验确定表面原子的种类，实验上由于生长条件不同可能有多种表面原子的情况，例如GaN(0001)的表面有Ga和N原子截止的不同情况。

第二，要找到面内的最小周期性单元。先通过晶胞找到解理面，找最小单元通常用蛮力法从小到大寻找，表面原子有不同的取法，对于每一种取法找到面内的最小单元，在不同表面原子取法中，找到最小单元中共同的最大的一个，即是要找的表面结构二维最小单元，为了实现这一算法，请关注github上的项目[SlabMaker](https://github.com/yyyu200/SlabMaker)，实际操作用MS的建模模块进行，而构造性的算法涉及空间群的十分复杂的分析。

第三，确定平板和真空的厚度。无论在平板内两个表面的距离，还是真空两边表面的距离都要足够大，以隔离两个表面的作用，模拟固体表面的性质，真空至少需要10Å到20Å。建议真空放在CELL的z方向的两端（如上图，垂直表面方向记为z）。有时，为了方便，Slab模型的CELL的基矢并不是正交的，但是考虑到周期性这种CELL与正交是等价的。有的文献描述平板厚度时，提到了**层**（layer）的概念，层并没有无争议的定义，需要依情况而定。有时，材料在垂直晶面方向有周期性，那么层可能是周期的个数；而另一些材料有若干层原子为一组，组与组之间距离较大可以明显划分开，这里的组就是层；还有的材料，在垂直晶面方向杂乱无章，一个原子或几个具有相同z坐标的原子就是一层。

下面以$\alpha-Al_{2}O_{3}$的(110)面为例，用ase和VESTA建slab模型（待续）。

注释

<span id = "note1">1.</span> 注意晶胞和原胞的区别，ibrav$\neq0$是用来设置原胞的，布拉伐格子中的7个简单格子本身也是晶体的原胞，而底心、面心、体心的7个布拉伐格子本身是晶胞，存在体积更小的原胞。

<span id = "note2">2.</span> trigonal三方晶系有两种布拉伐格子，一种是ibrav=5，菱方（rhombohedral）布拉伐格子，另一种是ibrav=4，六方（hexgonal）布拉伐格子，晶体属于菱方还是六方要看具体的空间群，在hexgonal和trigonal晶系中，7个空间群（$R3, R\overline{3}, R32, R3m, R3c, R\overline{3}m, R\overline{3}c$）具有菱方布拉伐格子的原胞，其余的45个空间群具有六方布拉伐格子的原胞。这里的菱方和六方是指晶体的格点系统lattice system，而非晶系，格点系统是按照布拉伐格子分类的，晶系是按照晶体点群分类的。

# References

1. International Tables for Crystallography (2006). Vol. A, Chapter 5.1, pp. 78–85.

2. https://en.wikipedia.org/wiki/Bravais_lattice

3. http://www.quantum-espresso.org/Doc/INPUT_PW.html

> 一部大书是一项大罪。 ——卡利马科斯 (Callimachus)

