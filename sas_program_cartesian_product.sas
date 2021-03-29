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

data b_table;
	input DL $ DL2020;
	datalines;
	DL1 1
	DL2 2
	DL3 3
	DL4 4
	;
run;

proc sql;
	create table cartesian_dl (drop=dl) as
	select *
	from a_table, b_table;
quit;