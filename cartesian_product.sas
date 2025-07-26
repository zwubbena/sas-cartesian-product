/**************************************************************************/
/* Program:    create_cartesian.sas 	     				  */																    */
/* Purpose:    Create all combinations of determination level      	  */
/*             from one year to the next year using a Cartesian product.  */
/**************************************************************************/

/*===============================================================*/ 
/*  SECTION 1: Dataset #1					 */																				*/ 
/*===============================================================*/ 
/*
   Create a lookup table for all possible 2019 determination levels (DL2019).
   Each DL code is mapped to a numeric level value.
*/
data a_table;
	input DL $ DL2019;
	datalines;
	DL0 0
	DL1 1
	DL2 2
	DL3 3
	DL4 4
	;
run;

/*===============================================================*/ 
/*  SECTION 2: Dataset #2					 */																				*/
/*===============================================================*/ 
/*
   Create a lookup table for all possible 2020 determination levels (DL2020).
   Each DL code is mapped to a numeric level value.
*/
data b_table;
	input DL $ DL2020;
	datalines;
	DL1 1
	DL2 2
	DL3 3
	DL4 4
	;
run;

/*===============================================================*/ 
/*  SECTION 3: Generate Cartesian Product 			 */													  */
/*===============================================================*/ 
/*
   Perform a cross join between a_table and b_table using PROC SQL.
   This creates all possible combinations of 2019 and 2020 determination levels.
   The duplicate DL variable is dropped to avoid redundancy.
*/
proc sql;
	create table cartesian_dl (drop=DL) as
	select *
	from a_table, b_table;
quit;

/**************************************************************************/
/*  SAS Program End							  */																										*/
/**************************************************************************/
