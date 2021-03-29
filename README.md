# SAS Cartesian Product

## 1. Introduction

If you're like me, you probably never could've imagined a scenario when you’d use the Cartesian product. So, I was surprised when I found it useful for solving a number of analytical problems when programming in [SAS](https://www.sas.com/en_us/home.html). 

Here I discuss using the Cartesian product in SAS to solve just one of those analytical problems:

-  ***How has a school district's determination level (DL) changed from one year to the next?***

This article is divided into six sections including the introduction.


## 2. Keywords

Below is a list of keywords and their definitions that you should be familiar with at the onset:
- ***SAS Language*** - is a computer programming language used for statistical analysis based on SAS (Statistical Analysis System), a statistical software suite developed by the SAS Institute.
- ***Ordered Pair*** - a pair of objects (denoted by: a,b) where one element is designated first and the other element is designated second. 
- ***Cartesian Product*** - the Cartesian product of two sets A and B, denoted A × B, is the set of all possible ordered pairs where the elements of A are first and the elements of B are second. 
- ***Determination Level*** - Each school district in Texas is assigned one of four determination levels (DLs) for their special education program: Meets Requirements = 1, Needs Assistance = 2, Needs Intervention, and Needs Substantial Intervention = 4. Such DL assignment denotes the degree to which a school district has implemented the Individuals with Disabilities Education Act (IDEA).

## 3. What is the Cartesian product?

The essence of the Cartesian product is that we can use sets to make new sets that contain all paired elements from the initial sets. What does that mean? Supposed we have two sets: A and B. And, each set contains elements. These elements could be anything but for this example we'll use letters. So set A has three elements: a, b, and c. And, set B has three elements: d, e, and f (see below). 

- ***A = {a,b,c}***
- ***B = {d,e,f}***

The Cartesian product allows us to find all combinations of the elements in set A and in set B. The Cartesian product of set A and set B is A x B, which creates a new set containing all paired combinations (or ordered pairs) from set A and set B. Because set A has 3 elements and set B has 3 elements, the Cartesian product contains a total of 9 ordered pairs: 3 x 3 = 9 (see below).

- ***A x B = {(a,d),(a,e),(a,f),(b,d),(b,e),(b,f),(c,d),(c,e),(c,f)}***

So, from set A and set B we created the Cartesian product A x B. The Cartesian product contains nine ordered pair combinations. That is, it contains all possible combinations of the elements from set A and the elements from set B. 

Now let's look at a scenario of when we would use the Cartesian product.

## 4. Scenario

In Texas, every K-12 school district that has a special education program is assigned one of four determination levels (DLs) annually: 

- ***Meets Requirements = 1***
- ***Needs Assistance = 2***
- ***Needs Intervention = 3***
- ***Needs Substantial Intervention = 4***

Such DL assignment denotes the degree to which a school district has implemented the federal Individuals with Disabilities Education Act (IDEA). Each DL is based on an equation that combines different indicators like graduation, dropout, etc. However, that's not relevant here. ***This scenario is about how a school district's DL has changed from one year to the next.*** 

Of course, if we're interested in one school district, we could look at their 2019 DL and their 2020 DL to know how their DL changed. But, when dealing with over a thousand districts, this becomes a task better suited for SAS programming, the Cartesian product, and conditional processing. But, we'll save conditional processing in SAS for another post.

## 5. SAS Programming

### 5.1. Dataset: 2019 DL Values 
The first step is to use SAS to create a data table of the 2019 DL values ranging from DL 0 to DL 4. The 2019 DL set and its elements can be expressed as:

- ***19DL = {0,1,2,3,4}***

#### 5.1.1. SAS Input
The SAS input code below starts with a `DATA` step and creates a dataset called `a_table`. The `INPUT`statement tells SAS to create a `DL` `$` character variable and to create a `DL2019` numeric variable . The `DATALINES` statement reads the subsequent lines of data directly into the SAS program (rather than coming from an external data source). Each of the five lines contain the data values for the variables in the `INPUT` statement. The `RUN` statement tells SAS to execute the preceding block of code to generate the new SAS dataset.
```
data a_table;
	input DL $  DL2019;
	datalines;
	DL0 0
	DL1 1
	DL2 2
	DL3 3
	DL4 4
	;
run;
```
#### 5.1.2. SAS Output
The below screenshot is the output from executing the preceding block of SAS code:
![output1](https://github.com/zanewubbena/cartesian-product-sas/blob/09efc365e072e1e29a48ae608fc53b4c75b90b15/SAS-Output/DL19.png)

### 5.2. Dataset: 2020 DL Values 
The second step is to use SAS to create a data table of the 2020 DL values. However, Unlike the 2019 DL values that ranged from DL 0 to DL 4, the 2020 DL values ranged from DL 1 to DL 4. The 2020 DL set and its elements can be expressed as:

- ***20DL = {1,2,3,4}***

#### 5.2.1. SAS Input
The SAS input code below starts with a `DATA` step and creates a dataset called `b_table`. The `INPUT`statement tells SAS to create a `DL` `$` character variable and to create a `DL2020` numeric variable . The `DATALINES` statement reads the subsequent lines of data directly into the SAS program (rather than coming from an external data source). Each of the five lines contain the data values for the variables in the `INPUT` statement. The `RUN` statement tells SAS to execute the preceding block of code to generate the new SAS dataset.
```
data b_table;
	input DL $ DL2020;
	datalines;
	DL1 1
	DL2 2
	DL3 3
	DL4 4
	;
run;
```
#### 5.2.2. SAS Output
The below screenshot is the output from executing the preceding block of SAS code:
![output2](https://github.com/zanewubbena/cartesian-product-sas/blob/09efc365e072e1e29a48ae608fc53b4c75b90b15/SAS-Output/DL20.png)

### 5.3. Cartesian Product (2019 DL Values x 2020 DL Values)
Now we have two datasets containing all DL values from 2019 and 2020. We'll use those datasets to create a new dataset of the Cartesian product of DL change from year-to-year. While `a_table` has five elements, `b_table` has four elements. Therefore, the Cartesian product of `a_table` and `b_table` is `a_table` x `b_table` or 5 x 4 = 20. So, there are 20 ordered pair combinations of DL change:

- ***19DL x 20DL = {(0,1),(0,2),(0,3),(0,4),(1,1),(1,2),(1,3),(1,4),(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(3,4),(4,1),(4,2),(4,3),(4,4)}***

#### 5.3.1. SAS Input
The SAS input code below starts with a `PROC SQL` step to join the two datasets together. 
```
proc sql;
	create table cartesian_dl (drop=DL) as
	select *
	from 
	    a_table, 
	    b_table
	;
quit;
```
#### 5.3.2. SAS Output
The below screenshot is the output from executing the preceding block of SAS code:
![output3](https://github.com/zanewubbena/cartesian-product-sas/blob/09efc365e072e1e29a48ae608fc53b4c75b90b15/SAS-Output/DL1920.png)

## 6. Cartesian Product

The Cartesian product allows us to see all the possible ways the DL values may have changed for a school district from one year to the next. Each district with a DL in both years meet one of the ordered pair combinations from the Cartesian product dataset.



Have a comment or question, email: [zwubbena@gmail.com](zwubbena@gmail.com).
