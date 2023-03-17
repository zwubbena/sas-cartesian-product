# SAS Cartesian Product

## 1. Introduction

Sometimes it's hard time imagining a scenario when you’d use the Cartesian product in [Education Data Scieince (EDS)](https://journals.sagepub.com/doi/full/10.1177/23328584211052055). However, [SAS](https://www.sas.com/en_us/home.html) programmers can use the Cartesian product as a means for solving a number of analytical problems. Here I discuss solving one of those problems:

-  ***How has a school district's determination level (DL) changed from one year to the next?***

This article is structured into six parts: introduction, keywords, Cartesian product, scenario, SAS programming, and determination level change.


## 2. Keywords

Below is a list of keywords and their definitions:
- **SAS Language** - is a computer programming language used for statistical analysis based on SAS (Statistical Analysis System), a statistical software suite developed by the SAS Institute.
- **Ordered Pair** - a pair of objects (denoted by: a,b) where one element is designated first and the other element is designated second. 
- **Cartesian Product** - the Cartesian product of two sets A and B, denoted A × B, is the set of all possible ordered pairs where the elements of A are first and the elements of B are second. 
- **Determination Level** - Each US school district is assigned one of four determination levels (DLs) for special education by their state education agency: Meets Requirements = 1, Needs Assistance = 2, Needs Intervention = 3, and Needs Substantial Intervention = 4.

## 3. Cartesian Product

What is the Cartesian product? The essence of the Cartesian product is that we can use sets to make a new set that contain all the paired elements from the initial sets. What does that mean? Let's break it down. A set is a collection of things with a common property. The things that make up a set are called elements. Supposed we have two sets: A and B. And, each set contains a series of elements. Let's use lower case letters, where set A has three elements: a, b, and c. And, set B has three elements: d, e, and f (see set notation below). 

- ***A = {a,b,c}***
- ***B = {d,e,f}***

The Cartesian product allows us to find all combinations of the elements in both set A and set B. Given sets A and B, we can multiply them together to produce a new set denoted as A x B. This operation is called the Cartesian product. This new set contains all the paired combinations (or ordered pairs) from set A and set B. Because set A has 3 elements and set B has 3 elements, the Cartesian product is 9 ordered pairs: 3 x 3 = 9 (see notation for the Cartesian product below).

- ***A x B = {(a,d),(a,e),(a,f),(b,d),(b,e),(b,f),(c,d),(c,e),(c,f)}***

So, from set A and set B we've created the Cartesian product A x B with nine ordered pairs. Those ordered pairs give all of the possible combinations of elements from both set A and set B. 

Now let's look at a scenario of when we would use the Cartesian product.

## 4. Scenario

Each K-12 U.S. school district that has a special education program is assigned one of four determination levels (DLs) annually by their state education agency: 

- **Meets Requirements (DL 1)**
- **Needs Assistance (DL 2)**
- **Needs Intervention (DL 3)**
- **Needs Substantial Intervention (DL 4)**

Such DL assignment denotes the degree to which a school district has implemented the federal Individuals with Disabilities Education Act (IDEA). For example, in Texas each DL is based on an equation that combines different indicators like graduation, dropout, etc. However, that's not relevant here but you can read more about the [RDA system](https://tea.texas.gov/academics/special-student-populations/review-and-support/results-driven-accountability-rda). 

***This scenario is about how a school district's DL has changed from one year to the next.*** 

Of course, if we're interested in one school district, we could look at their 2019 DL and their 2020 DL to know how their DL changed. But, when dealing with over a thousand districts, this becomes a task better suited for SAS programming, the Cartesian product, and conditional processing.

## 5. SAS Programming

### 5.1. Dataset: 2019 DL Values 
The first step is to use SAS to create a data table of the 2019 DL values. The values ranged from DL 0 to DL 4. The 2019 DL set and its elements can be expressed as:

- ***19DL = {0,1,2,3,4}***

#### 5.1.1. SAS Input
The SAS code below starts with a `DATA` step and creates a dataset called `a_table`. The `INPUT`statement tells SAS to create a `DL` variable that's a character data type, denoted by `$`, and a numeric variable called `DL2019`. The `DATALINES` statement reads the subsequent lines of data directly into the SAS program (rather than coming from an external data source). Each of the five lines starting with `DL1` `1` contain the data values for the two variables in the `INPUT` statement. The `RUN` statement tells SAS to execute the preceding block of code to generate the new SAS dataset.
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
The screenshot below is the output from executing the preceding block of SAS code:
![output1](https://github.com/zanewubbena/cartesian-product-sas/blob/09efc365e072e1e29a48ae608fc53b4c75b90b15/SAS-Output/DL19.png)

### 5.2. Dataset: 2020 DL Values 
The second step is to use SAS to create a data table of the 2020 DL values. However, Unlike the 2019 DL values that ranged from DL 0 to DL 4, the 2020 DL values ranged from DL 1 to DL 4. The 2020 DL set and its elements can be expressed as:

- ***20DL = {1,2,3,4}***

#### 5.2.1. SAS Input
The SAS code below starts with a `DATA` step and creates a dataset called `b_table`. The `INPUT`statement tells SAS to create a `DL` `$` character variable and a `DL2020` numeric variable. The `DATALINES` statement reads the subsequent lines of data directly into the SAS program (rather than coming from an external data source). Each of the five lines starting with `DL1` `1` contain the data values for the two variables in the `INPUT` statement. The `RUN` statement tells SAS to execute the preceding block of code to generate the new SAS dataset.
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
The screenshot below is the output from executing the preceding block of SAS code:
![output2](https://github.com/zanewubbena/cartesian-product-sas/blob/09efc365e072e1e29a48ae608fc53b4c75b90b15/SAS-Output/DL20.png)

### 5.3. Cartesian Product (2019 DL Values x 2020 DL Values)
Now we have two datasets containing all DL values from 2019 and 2020. We'll use those datasets to create a new dataset of the Cartesian product of DL change from year-to-year. While `a_table` has five elements, `b_table` has four elements. Therefore, the Cartesian product of `a_table` and `b_table` is `a_table` x `b_table` or 5 x 4 = 20. So, there are 20 ordered pair combinations of DL change:

- ***19DL x 20DL = {(0,1),(0,2),(0,3),(0,4),(1,1),(1,2),(1,3),(1,4),(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(3,4),(4,1),(4,2),(4,3),(4,4)}***

#### 5.3.1. SAS Input
The SAS code below starts with a `PROC SQL` step to join the two datasets together from a query. The `CREATE TABLE` statement with the `AS` keyword creates a dataset called `cartesian_dl`. The asterisk `*` in the `SELECT` statement tells SAS to include all columns from both the `a_table` and the `b_table` datasets in the `FROM` clause. The `DROP=` option is associated with the output dataset `cartesian_dl`, which means that SAS will not write the `DL` variable to the output `cartesian_dl` dataset because for our purposes we're only interested in the DL2019 and the DL2020 columns. The `QUIT` statement ends the `PROC SQL` procedure.
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
The screenshot below is the output from executing the preceding block of SAS code:
![output3](https://github.com/zanewubbena/cartesian-product-sas/blob/09efc365e072e1e29a48ae608fc53b4c75b90b15/SAS-Output/DL1920.png)

## 6. Determination Level Change

The Cartesian product allows us to see all the possible ways the DL values may have changed for a school district from one year to the next. Each school district with a DL in both years must meet one of the ordered pair combinations from the Cartesian product dataset. Then we can assess if the school district's DL increased, decreased, or didn't change from year-to-year.

We can use SAS programming and conditional logic to create a new variable `DeterminationLevelChange`, and we can use the Cartesian product to account for every possible DL change combination, which I'll cover in my next GitHub article when time permits. 

[Conditional Logic in SAS](https://github.com/zanewubbena/conditional-logic-sas).

## 7. References
- [PennState - "Reading Instream Data"](https://online.stat.psu.edu/stat480/lesson/2/2.1)
- [Math LibreTexts, "The Cartesian Product"](https://math.libretexts.org/Bookshelves/Mathematical_Logic_and_Proof/Book%3A_Book_of_Proof_(Hammack)/01%3A_Sets/1.02%3A_The_Cartesian_Product)
- [MathisFun, "Introduction to Sets"](https://www.mathsisfun.com/sets/sets-introduction.html)
- [SAS Documentation, "Asterisk ("*") Notation"](https://documentation.sas.com/?cdcId=pgmsascdc&cdcVersion=9.4_3.5&docsetId=sqlproc&docsetTarget=n0mo9ak7pmhfjhn1fw5crkp17jg0.htm&locale=en#n0kj38z97ix6pun11kjnz44v3b41)
- [SAS Documentation, "About Creating a SAS Data Set with a DATA Step"](https://documentation.sas.com/?cdcId=pgmsascdc&cdcVersion=9.4_3.5&docsetId=lrcon&docsetTarget=n1xrpfyevzkdaen1m1meb5z8qwc6.htm&locale=en)
- [SAS Documentation, "Creating Tables"](https://documentation.sas.com/?cdcId=pgmsascdc&cdcVersion=9.4_3.5&docsetId=sqlproc&docsetTarget=p1l9ypkml4febvn0zsbkwev7v5x9.htm&locale=en)
- [SAS Documentation, "DROP="](https://v8doc.sas.com/sashtml/lgref/z0131113.htm)
- [SAS Documentation, "INFORMAT Statement"](https://documentation.sas.com/?cdcId=pgmsascdc&cdcVersion=9.4_3.5&docsetId=lestmtsref&docsetTarget=p164164hob450kn1agkpcosya669.htm&locale=en)
- [SAS Documentation, "The HPDS2 Procedure"](https://documentation.sas.com/?cdcId=pgmsascdc&cdcVersion=9.4_3.5&docsetId=prochp&docsetTarget=prochp_hpds2_syntax05.htm&locale=en)
- [SAS Documentation, "Using the DROP= and KEEP= Data Set Options for Efficiency"](https://documentation.sas.com/?cdcId=pgmsascdc&cdcVersion=9.4_3.5&docsetId=basess&docsetTarget=p10jjd7e6qn396n1a22uvw3va3ao.htm&locale=en)
- [SAS Support, "MERGING vs. JOINING: Comparing the DATA Step with SQL"](https://support.sas.com/resources/papers/proceedings/proceedings/sugi30/249-30.pdf)
- [SAS Support, "Sample 25270: Using PROC SQL to generate the Cartesian Product"](https://support.sas.com/kb/25/270.html)
- [SASnrd, "SAS Cartesian Product with PROC SQL and the Data Step"](https://sasnrd.com/sas-cartesian-product-proc-sql-data-step/)
- [UCLA, "Inputing Data into SAS"](https://stats.idre.ucla.edu/sas/modules/inputting-data-into-sas/)
- [web.mnstate.edu, "The Language of Sets — Cartesian Product"](http://web.mnstate.edu/peil/MDEV102/U1/S7/Cartesian4.htm)
- [Wikipedia, "Cartesian product"](https://simple.wikipedia.org/wiki/Cartesian_product)
