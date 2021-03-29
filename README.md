# SAS Cartesian Product

If you're like me, then you probably never could've imagined a scenario when you’d use the Cartesian product. So, I was quite surprised when I found the Cartesian product useful for solving a number of analytical problems when programming in [SAS](https://www.sas.com/en_us/home.html). 

Here I discuss using the Cartesian product in SAS to solve just one of those problems. 

## What is the Cartesian product?

The essence of the Cartesian product is that we can use sets to make new sets that contain all paired elements from the initial sets. What does that mean? Supposed we have two sets: A and B. Each set contains elements. These elements could be anything but for this example we'll use letters. So set A has three elements a, b, and c. And, set B has three elements, d, e, and f. 

Take a look below:

A = {a, b, c}

B = {d, e, f}

The Cartesian product allows us to find all possible combinations of the elements contained in both set A and set B. The Cartesian product of set A and set B is A x B, which creates a new set that contains all paired combinations (or ordered pairs) from set A and set B. Because set A had 3 elements and set B has 3 elements, there are a total of 9 ordered pairs (3 x 3 = 9).

A x B = {(a,d),(a,e),(a,f),(b,d),(b,e),(b,f),(c,d),(c,e),(c,f)}

So from set A and set B we created the Cartesian product A x B. The Cartesian product contains nine ordered pair combinations. That is, it contains all possible combinations of the elements from set A and the elements from set B.

## Scenario



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
