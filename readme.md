# SAS Cartesian Product

If you're like me, then you probably never could've imagined a scenario when you’d use the Cartesian product. So, I was quite surprised when I found the Cartesian product useful for solving a number of analytical problems when programming in [SAS](https://www.sas.com/en_us/home.html). 

Here I discuss using the Cartesian product in SAS to solve just one of those analytical problems. 

## Keywords

- ***SAS Language*** - is a computer programming language used for statistical analysis based on SAS (Statistical Analysis System), a statistical software suite developed by the SAS Institute.
- ***Ordered Pair*** - a pair of objects (denoted by: a,b) where one element is designated first and the other element is designated second. 
- ***Cartesian Product*** - the Cartesian product of two sets A and B, denoted A × B, is the set of all possible ordered pairs where the elements of A are first and the elements of B are second. 
- ***Determination Level*** - Each school district in Texas is assigned one of four determination levels (DLs) for their special education program: Meets Requirements = 1, Needs Assistance = 2, Needs Intervention, and Needs Substantial Intervention = 4. Such DL assignment denotes the degree to which a school district has implemented the Individuals with Disabilities Education Act (IDEA).

## What is the Cartesian product?

The essence of the Cartesian product is that we can use sets to make new sets that contain all paired elements from the initial sets. What does that mean? Supposed we have two sets: A and B. And, each set contains elements. These elements could be anything but for this example we'll use letters. So set A has three elements a, b, and c. And, set B has three elements, d, e, and f (see below). 

- ***A = {a, b, c}***
- ***B = {d, e, f}***

The Cartesian product allows us to find all possible combinations of the elements in set A and in set B. The Cartesian product of set A and set B is A x B, which creates a new set containing all paired combinations (or ordered pairs) from set A and set B. Because set A has 3 elements and set B has 3 elements, the Cartesian product contains a total of 9 ordered pairs: 3 x 3 = 9 (see below).

- ***A x B = {(a,d),(a,e),(a,f),(b,d),(b,e),(b,f),(c,d),(c,e),(c,f)}***

So, from set A and set B we created the Cartesian product A x B. The Cartesian product contains nine ordered pair combinations. That is, it contains all possible combinations of the elements from set A and the elements from set B. Now let's look at a scenario when we would use the Cartesian product.

## Scenario

I'll provide an overview of such a scenario now to answer this question.




Create table of all possible 2019 determination level (DL) values
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


Create table of all possible 2020 determination level (DL) values

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

Create the cartesian product using both 2019 DLs and 2020 DLs

```
proc sql;
	create table cartesian_dl (drop=DL) as
	select *
	from a_table, b_table;
quit;
```

Have a comment or question, email me: zwubbena@gmail.com.
