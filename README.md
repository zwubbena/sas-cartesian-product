# SAS Cartesian Product

If you're like me, then you probably never could've imagined a time or scenario when you’d need to use the Cartesian product. So, I was surprised when I found the Cartesian product quite useful for a number of analytical problems I faced.

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
