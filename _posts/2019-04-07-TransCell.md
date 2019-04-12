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

保持平移对称性和点群对称性的最小单元是**晶胞**。

按照基元+格子的概念，确定**布拉伐格子**应满足：（1）所选平行六面体必须充分反映出格子的点群与平移群，即平行六面体必须与整个格子的晶系特征一致。（2）所选择平行六面体各个棱之间夹角为直角的数目最多，不为直角者尽可能地接近直角。（3）在满足上述（1）（2）条件后，所选择的平行六面体的体积应为最小。布拉伐格子即为晶胞。3维空间的布拉伐格子有14种。

<p align="center">
    <img src="http://yyyu200.github.io/DFTbook/img/BravaisLattices.png" width="563" />
</p>

在特定的平移、旋转操作下，晶体保持不变，这种在某种操作下不变的性质称之为体系的对称性，不同的操作定义了不同的对称性，例如，沿$\vec a$方向平移2个平移基矢等。体系的薛定谔方程，由于体系的对称性，也具有变换下不变的性质，于是有量子数来标记这些变换，晶体平移对称性是一系列准连续的k值所标记的，k点所在空间称为k空间，k空间是相对晶体的原胞定义的，计算晶体的能带就是在k空间进行的，k空间也具有周期性，取原点周围的魏格纳-塞茨原胞，称为第一**布里渊区**。

**晶面**是相对于晶胞定义的。

14种布拉伐格子，按照具有的点群分类，分为7种**晶系**，即：

triclinic, monoclinic, orthorhombic, tetragonal, rhombohedral, hexagonal, and cubic。

其中rhombohedral有两种晶胞表示，一种是菱方，一种是六方，六方体积是菱方的三倍，在QE输入中有专门的设定。


# QE中的结构定义

QE计算的结构都是在三维空间中周期性重复的，所以需要定义一个周期性的单元，一般是一个平行六面体的三个基矢量，另外需要定义周期性单元内的原子坐标。QE中的结构定义有ibrav等于零和ibrav不等于零两种方式，这两种方式首先确定了CELL，这里的CELL是指所要计算的周期性结构单元，但不一定是最小的。

ibrav不等于零时，这里建议只用来计算材料的原胞，这时，ibrav的值代表布拉伐格子的类型，但是，注意ibrav=4定义的是六方的晶胞而不是原胞。

设置ibrav=0，这时需要在输入文件中写入CELL_PARAMETERS，即CELL晶格的基矢量，这种方法可以用来设置超胞、slab模型等。

在定义了CELL之后，用ATOMIC_POSITIONS定义CELL中原子的坐标。

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

# 超胞近似

分子、团簇、纳米晶体、具有点缺陷的固体等不具有整体的周期性，纳米线是1维周期性的，固体表面、量子阱、二维材料等是2维周期性的，QE这样的基于平面波基函数的程序，对于这些非三维周期性的材料需要采取**超胞**近似，选取足够大的周期单元，并且，需要时在CELL中的一部分空间不加入任何原子，也就是引入真空，以隔离非周期性的维度。

注释

## References

1. International Tables for Crystallography (2006). Vol. A, Chapter 5.1, pp. 78–85.

