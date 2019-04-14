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

# 晶体结构简介

先哲卡利马科斯 (Callimachus) 曾经言道：“一部大书是一项大罪”。就罪过而言，希望我写这本密度泛函计算的书是一本小书。而我今天介绍的这本大书：International Tables for Crystallography（ITC），ITC包括9卷，7000多页，希望如其名，只是一些表格，而被豁免。

首先，我试图说明以下几个概念：

平移群，点群，空间群，晶体，原胞，晶胞，布拉伐格子，晶系，晶面，布里渊区。

**群**，是一种代数结构，在集合上封闭的运算，运算满足结合律，存在单位元，存在逆元，定义为群。

**晶体**，是自然形成和人工合成的固体的形态，大量原子周期性排列则为晶体，由于结合能最低，纯净物在熔融条件下缓慢降温会自发形成晶体。

可以将空间中的晶体坐标看成集合，在考虑块材性质时，可以认为晶体在空间无限延伸，允许其转动、平移，则可以构成群，转动、反演为群的运算，或称之为变换、操作。

如果只允许平移，称为**平移群**。

如果只允许转动（含空间反演、镜像），称为**点群**，3维空间中的点群有32种。

如果允许转动和平移的复合操作，称为**空间群**，3维空间中的空间群有230种。指定了空间群的类型，我们只需要知道在空间群操作下不重复的原子位置，就可以确定晶体结构，这些不重复的位置称为Wyckoff位置，QE输入有space_group和ATOMIC_POSITIONS { crystal_sg }来专门设置。

保持平移对称性的最小单元是**原胞**。

保持平移对称性和点群对称性的最小单元是**晶胞**。

按照基元+格子的概念，确定**布拉伐格子**应满足：（1）所选平行六面体必须充分反映出格子的点群与平移群，即平行六面体必须与整个格子的晶系特征一致。（2）所选择平行六面体各个棱之间夹角为直角的数目最多，不为直角者尽可能地接近直角。（3）在满足上述（1）（2）条件后，所选择的平行六面体的体积应为最小。布拉伐格子即为晶胞。3维空间的布拉伐格子有14种。[下表](https://en.wikipedia.org/wiki/Bravais_lattice)是14种布拉伐格子的基矢a,b,c及夹角$\alpha, \beta, \gamma$所具有的特定关系。

<p align="center">
    <img src="https://yyyu200.github.io/DFTbook/img/BravaisLattices.png" width="563" />
</p>

在特定的平移、旋转操作下，晶体保持不变，这种在某种操作下不变的性质称之为体系的对称性，不同的操作定义了不同的对称性，例如，沿$\vec a$方向平移2个平移基矢等。体系的薛定谔方程，由于体系的对称性，也具有变换下不变的性质，于是有量子数来标记这些变换，晶体平移对称性是一系列准连续的k值所标记的，k点所在空间称为k空间，k空间是相对晶体的原胞定义的，计算晶体的能带就是在k空间进行的，k空间也具有周期性，取原点周围的魏格纳-塞茨原胞，称为第一**布里渊区**。

**晶面**是相对于晶胞定义的。

14种布拉伐格子，按照具有的点群分类，分为7种**晶系**，即：

triclinic, monoclinic, orthorhombic, tetragonal, rhombohedral, hexagonal, and cubic。

其中rhombohedral有两种晶胞表示，一种是菱方，一种是六方，六方体积是菱方的三倍，在QE输入中有专门的设定。


# QE中的结构定义

QE输入文件的总体结构如下图，与结构有关的包括CONTROL部分的```ibrav,celldm,nat,ntyp```以及```ATOMIC_POSITIONS```和```CELL_PARAMETERS```两部分。

<p align="center">
    <img src="https://yyyu200.github.io/DFTbook/img/structure_input.png" width="503" />
</p>

QE计算的结构都是在三维空间中周期性重复的，所以需要定义一个周期性的单元，一般是一个平行六面体的三个基矢量，另外需要定义周期性单元内的原子坐标。QE中的结构定义首先确定了CELL，这里的CELL是指所要计算的周期性结构单元。在QE中用三个矢量$\vec{v_{1}},\vec{v_{2}},\vec{v_{3}}$定义CELL。CELL的定义不依赖于**空间直角坐标系**（**笛卡尔坐标系**）的选择，只需要定义三个基矢量的长度和三个夹角，但是为了计算，需要确定一个空间直角坐标系，以写出各个矢量的笛卡尔坐标，

$$\vec{v_{1}}=(v_{11},v_{12},v_{13}),\vec{v_{2}}=(v_{21},v_{22},v_{23}),\vec{v_{3}}=(v_{31},v_{32},v_{33})$$，

这里空间直角坐标系的选取，对于ibrav$\neq$0是在QE程序内部进行的，对于ibrav=0是用户通过CELL_PARAMETERS而确定的。

ibrav不等于零时，这里建议只用来计算材料的原胞，这时，ibrav的值代表布拉伐格子的类型。下面的表格列出了各种布拉伐格子的celldm设置以及对应的$\vec{v_{1}},\vec{v_{2}},\vec{v_{3}}$晶格矢量（相当于内部生成的CELL_PARAMETERS），注意celldm(1)定义了alat，单位只能是Bohr；celldm(2)和celldm(3)定义的是比例b/a和c/a，而不是基矢长度，celldm(4:6)是角度的余弦值；对于ibrav$\neq$0，生成的是布拉伐格子的原胞；对于ibrav=5和ibrav=-5，是Trigonal三方（同Rhombohedral菱方）原胞的两种空间直角坐标系的取法，ibrav=5，六方轴沿z方向，而ibrav=-5，六方轴沿(111)方向；对于ibrav=12和ibrav=-12，是简单单斜原胞的两种空间直角坐标系的取法。

设置ibrav=0，这时需要在输入文件中写入CELL_PARAMETERS，即CELL晶格的基矢量$\vec{v_{1}},\vec{v_{2}},\vec{v_{3}}$，基矢量是空间直角坐标系中的直角坐标（笛卡尔坐标），空间直角坐标系的选法有一定的任意性，用户可以根据习惯选择，坐标的单位有三种选择：alat，bohr，angstrom，其中，alat是由celldm(1)或A定义，注意CELL_PARAMETERS这种方法可以用来设置超胞、slab模型等。

在定义了CELL之后，用ATOMIC_POSITIONS定义CELL中原子的坐标。ATOMIC_POSITIONS的单位有以下可供选择\{ alat \| bohr \| angstrom \| crystal \| crystal_sg \}，其中，crystal是指以$\vec{v_{1}},\vec{v_{2}},\vec{v_{3}}$为基矢量的分数坐标，$\vec{X}=(x_{1},x_{2},x_{3})=x_{1}\vec{v_{1}}+x_{2}\vec{v_{2}}+x_{3}\vec{v_{3}}$。

在QE中还可以直接给出晶格的基矢长度和夹角A, B, C, cosAB, cosAC, cosBC，单位是Angstrom，这样唯一确定了CELL，同样定义了$\vec{v_{1}},\vec{v_{2}},\vec{v_{3}}$，这时的空间直角坐标系是QE内部定义的，也由下面表格给出。注意这里A，B，C的顺序要按照表格，夹角余弦顺序也不能出错；ibrav=0时，A和celldm(1)设置一个作为alat。

QE提供多种方式完成一件任务的设计风格，对于具有各种习惯的用户提供了得心应手的工具，但是对于初学者难免有一种眼花缭乱的感觉，这里对于初学者推荐一种通用的方法定义CELL，即设置ibrav=0，celldm(1)= 1 / 0.52917720859 = 1.88972613289 ，将alat设置成 1.88972613289 Bohr=1.0 Angstrom （1 Bohr = 0.52917720859 Angstrom），显式地写出以Angstrom为单位的CELL_PARAMETER {alat}，对于ATOMIC_POSITIONS建议使用分数坐标，分数坐标的三个分量值建议保持在0到1之间，更符合习惯。

最后，强烈建议做好结构之后，用可视化的软件如VESTA、Xcrysden、MS等画出晶体结构，检查一下原子间距等是否正确，这些软件并不都支持QE的输入格式，可能需要转换格式。

```
ibrav      structure                   celldm(2)-celldm(6)
                                     or: b,c,cosab,cosac,cosbc
  0          free
      crystal axis provided in input: see card CELL_PARAMETERS

  1          cubic P (sc)
      v1 = a(1,0,0),  v2 = a(0,1,0),  v3 = a(0,0,1)

  2          cubic F (fcc)
      v1 = (a/2)(-1,0,1),  v2 = (a/2)(0,1,1), v3 = (a/2)(-1,1,0)

  3          cubic I (bcc)
      v1 = (a/2)(1,1,1),  v2 = (a/2)(-1,1,1),  v3 = (a/2)(-1,-1,1)

  4          Hexagonal and Trigonal P        celldm(3)=c/a
      v1 = a(1,0,0),  v2 = a(-1/2,sqrt(3)/2,0),  v3 = a(0,0,c/a)

  5          Trigonal R, 3fold axis c        celldm(4)=cos(alpha)
      The crystallographic vectors form a three-fold star around
      the z-axis, the primitive cell is a simple rhombohedron:
      v1 = a(tx,-ty,tz),   v2 = a(0,2ty,tz),   v3 = a(-tx,-ty,tz)
      where c=cos(alpha) is the cosine of the angle alpha between
      any pair of crystallographic vectors, tx, ty, tz are:
        tx=sqrt((1-c)/2), ty=sqrt((1-c)/6), tz=sqrt((1+2c)/3)
 -5          Trigonal R, 3fold axis <111>    celldm(4)=cos(alpha)
      The crystallographic vectors form a three-fold star around
      <111>. Defining a' = a/sqrt(3) :
      v1 = a' (u,v,v),   v2 = a' (v,u,v),   v3 = a' (v,v,u)
      where u and v are defined as
        u = tz - 2*sqrt(2)*ty,  v = tz + sqrt(2)*ty
      and tx, ty, tz as for case ibrav=5
      Note: if you prefer x,y,z as axis in the cubic limit,
            set  u = tz + 2*sqrt(2)*ty,  v = tz - sqrt(2)*ty
            See also the note in Modules/latgen.f90

  6          Tetragonal P (st)               celldm(3)=c/a
      v1 = a(1,0,0),  v2 = a(0,1,0),  v3 = a(0,0,c/a)

  7          Tetragonal I (bct)              celldm(3)=c/a
      v1=(a/2)(1,-1,c/a),  v2=(a/2)(1,1,c/a),  v3=(a/2)(-1,-1,c/a)

  8          Orthorhombic P                  celldm(2)=b/a
                                             celldm(3)=c/a
      v1 = (a,0,0),  v2 = (0,b,0), v3 = (0,0,c)

  9          Orthorhombic base-centered(bco) celldm(2)=b/a
                                             celldm(3)=c/a
      v1 = (a/2, b/2,0),  v2 = (-a/2,b/2,0),  v3 = (0,0,c)
 -9          as 9, alternate description
      v1 = (a/2,-b/2,0),  v2 = (a/2, b/2,0),  v3 = (0,0,c)

 10          Orthorhombic face-centered      celldm(2)=b/a
                                             celldm(3)=c/a
      v1 = (a/2,0,c/2),  v2 = (a/2,b/2,0),  v3 = (0,b/2,c/2)

 11          Orthorhombic body-centered      celldm(2)=b/a
                                             celldm(3)=c/a
      v1=(a/2,b/2,c/2),  v2=(-a/2,b/2,c/2),  v3=(-a/2,-b/2,c/2)

 12          Monoclinic P, unique axis c     celldm(2)=b/a
                                             celldm(3)=c/a,
                                             celldm(4)=cos(ab)
      v1=(a,0,0), v2=(b*cos(gamma),b*sin(gamma),0),  v3 = (0,0,c)
      where gamma is the angle between axis a and b.
-12          Monoclinic P, unique axis b     celldm(2)=b/a
                                             celldm(3)=c/a,
                                             celldm(5)=cos(ac)
      v1 = (a,0,0), v2 = (0,b,0), v3 = (c*cos(beta),0,c*sin(beta))
      where beta is the angle between axis a and c

 13          Monoclinic base-centered        celldm(2)=b/a
                                             celldm(3)=c/a,
                                             celldm(4)=cos(ab)
      v1 = (  a/2,         0,                -c/2),
      v2 = (b*cos(gamma), b*sin(gamma), 0),
      v3 = (  a/2,         0,                  c/2),
      where gamma is the angle between axis a and b

 14          Triclinic                       celldm(2)= b/a,
                                             celldm(3)= c/a,
                                             celldm(4)= cos(bc),
                                             celldm(5)= cos(ac),
                                             celldm(6)= cos(ab)
      v1 = (a, 0, 0),
      v2 = (b*cos(gamma), b*sin(gamma), 0)
      v3 = (c*cos(beta),  c*(cos(alpha)-cos(beta)cos(gamma))/sin(gamma),
           c*sqrt( 1 + 2*cos(alpha)cos(beta)cos(gamma)
                     - cos(alpha)^2-cos(beta)^2-cos(gamma)^2 )/sin(gamma) )
      where alpha is the angle between axis b and c
             beta is the angle between axis a and c
            gamma is the angle between axis a and b
```

# 非周期性系统

分子、团簇、纳米晶体、具有点缺陷的固体等不具有周期性，纳米线是1维周期性的，固体表面、量子阱、二维材料等是2维周期性的，QE这样的基于平面波基函数的程序，对于这些非三维周期性的材料需要采取**超胞**近似，选取足够大的周期单元，并且，需要时在CELL中的一部分空间不加入任何原子，也就是引入真空，以隔离非周期性的维度。

# 平板（slab）模型的建立

对于固体表面，平面波计算要首先建立平板模型，选取垂直晶面方向足够厚的平板，并且加入足够厚的真空，以消除表面之间的作用，实现表面性质的计算。对于异质结构，如超晶格，以及二维材料异质结，如双层石墨烯“魔角”，模型建立也会遇到有共性的问题。

对于有重构（也叫再构，reconstruction）的晶体表面，要按照重构截取面内的原胞。对于没有重构的晶体表面，需要考虑如下：

首先，确定要计算的晶面，晶面用密勒指数标记，注意密勒指数是相对晶胞定义的，通常是三个数，如(001)，(110), (531)等等，对于六方和三方（菱方）晶体也用四个数的密勒指数，如(0001),(1-101)等，这里是选了六方的面内3个基矢以及沿着六方（三方）轴的1个基矢，一共4个基矢而定义的密勒指数，其中前三个指数的和一定是0，所以只有3个独立的指数，有的地方对于六方结构的晶面也用三指数的表示。

第二，要找到面内的最小周期性单元，先通过晶胞找到解理面，找最小单元通常用蛮力法从小到大寻找，表面原子有不同的取法，对于每一种取法找到面内的最小单元，在不同表面原子取法中，找到最小单元中共同的最大的一个，即是要找的表面结构二维最小单元，为了实现这一算法，请关注github上的项目[SlabMaker](https://github.com/yyyu200/SlabMaker)，实际操作用MS的建模模块进行，而构造性的算法涉及空间群的十分复杂的分析。

第三，确定平板和真空的厚度，无论在平板内两个表面的距离，还是真空两边表面的距离都要足够大，以隔离两个表面的作用，模拟固体表面的性质，真空至少需要10A到20A。建议真空放在CELL的z方向的两端。有的文献描述平板厚度时，提到了**层**（layer）的概念，层并没有无争议的定义，需要依情况而定。有时，材料在垂直晶面方向有周期性，那么层可能是周期的个数；而另一些材料有若干层原子为一组，组与组之间距离较大可以明显划分开，这里的组就是层；还有的材料，在垂直晶面方向杂乱无章，一个原子就是一层。

下面以$\alpha-Al_{2}O_{3}$的(110)面为例，用ase和VESTA建slab模型。

注释

## References

1. International Tables for Crystallography (2006). Vol. A, Chapter 5.1, pp. 78–85.

2. https://en.wikipedia.org/wiki/Bravais_lattice

3. http://www.quantum-espresso.org/Doc/INPUT_PW.html
