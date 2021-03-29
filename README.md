# SAS Cartesian Product

If you're like me, then you probably never could've imagined a scenario when you’d use the Cartesian product. So, I was quite surprised when I found the Cartesian product useful for solving a number of analytical problems when programming in [SAS](https://www.sas.com/en_us/home.html). 

Here I discuss using the Cartesian product in SAS to solve just one of those analytical problems:

-  How has a school district's determination levle (DL) changed from one year to the next year?


## Keywords

Below is a list of keywords and their definitions that you should be familiar with at the onset:
- ***SAS Language*** - is a computer programming language used for statistical analysis based on SAS (Statistical Analysis System), a statistical software suite developed by the SAS Institute.
- ***Ordered Pair*** - a pair of objects (denoted by: a,b) where one element is designated first and the other element is designated second. 
- ***Cartesian Product*** - the Cartesian product of two sets A and B, denoted A × B, is the set of all possible ordered pairs where the elements of A are first and the elements of B are second. 
- ***Determination Level*** - Each school district in Texas is assigned one of four determination levels (DLs) for their special education program: Meets Requirements = 1, Needs Assistance = 2, Needs Intervention, and Needs Substantial Intervention = 4. Such DL assignment denotes the degree to which a school district has implemented the Individuals with Disabilities Education Act (IDEA).

## What is the Cartesian product?

The essence of the Cartesian product is that we can use sets to make new sets that contain all paired elements from the initial sets. What does that mean? Supposed we have two sets: A and B. And, each set contains elements. These elements could be anything but for this example we'll use letters. So set A has three elements a, b, and c. And, set B has three elements, d, e, and f (see below). 

- ***A = {a, b, c}***
- ***B = {d, e, f}***

The Cartesian product allows us to find all combinations of the elements in set A and in set B. The Cartesian product of set A and set B is A x B, which creates a new set containing all paired combinations (or ordered pairs) from set A and set B. Because set A has 3 elements and set B has 3 elements, the Cartesian product contains a total of 9 ordered pairs: 3 x 3 = 9 (see below).

- ***A x B = {(a,d),(a,e),(a,f),(b,d),(b,e),(b,f),(c,d),(c,e),(c,f)}***

So, from set A and set B we created the Cartesian product A x B. The Cartesian product contains nine ordered pair combinations. That is, it contains all possible combinations of the elements from set A and the elements from set B. 

Now let's look at a scenario of when we would use the Cartesian product.

## Scenario

In Texas, every K-12 school district that has a special education program is annually assigned one of four determination levels (DLs): 

- ***Meets Requirements = 1***
- ***Needs Assistance = 2***
- ***Needs Intervention = 3***
- ***Needs Substantial Intervention = 4***

Such DL assignment denotes the degree to which a school district has implemented the federal Individuals with Disabilities Education Act (IDEA). Each DL is based on an equation that combines different indicators like graduation, dropout, etc. However, that's not relevant here. ***This scenario is about how a school district's DL had changed from one year to the next.*** 

Of course, if we're just looking at one school district, we could just look at their 2020 DL and their 2021 DL to know how that DL has changed or not from one year to the next. But, when dealing with over a thousand school districts, this becomes a task better suited for SAS programming, the Cartesian product, and conditional processing.

## Cartesian Product of Determination Levels

The first step is to create a data tables of all 2019 DL values. The values range from DL 0 to DL 4 (see code below):
#### Input
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
#### Output

![Output](https://github.com/zanewubbena/cartesian-product-sas/blob/52e4849a5bb42c2ac48171fb1720afd72845b695/SAS-Output/Screen%20Shot%202021-03-29%20at%201.19.05%20PM.png)


The second step is to create another data tables of all 2020 DL values. Unlike the 2019 DL values that ranged from DL 0 to DL 4, the 2020 DL values ranged from DL 1 to DL 4 (see code below):
#### Input
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
#### Output
![Output](https://github.com/zanewubbena/cartesian-product-sas/blob/52e4849a5bb42c2ac48171fb1720afd72845b695/SAS-Output/Screen%20Shot%202021-03-29%20at%201.19.25%20PM.png)

Now that we have two data tables containing all possible DL values for 2019 and 2020, we'll use those tables to create the Cartesian product of DL change from 2019 to 2020. While the first table (a_table) has five elements, the second table (b_table) has four elements. Therefore, the Cartesian product of a_table and b_table is a_table x b_table or 5 x 4 = 20. So there should be 20 ordered pair combinations of DL change.

#### Input
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
#### Output`
![Output](https://github.com/zanewubbena/cartesian-product-sas/blob/52e4849a5bb42c2ac48171fb1720afd72845b695/SAS-Output/Screen%20Shot%202021-03-29%20at%201.18.35%20PM.png)

## Determination Level Change

Have a comment or question, email me: zwubbena@gmail.com.
