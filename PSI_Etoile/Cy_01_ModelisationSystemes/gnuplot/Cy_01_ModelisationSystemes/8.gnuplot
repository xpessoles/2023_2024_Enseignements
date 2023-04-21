set table "gnuplot/Cy_01_ModelisationSystemes/8.table"; set format "%.5f"
set samples 100.0; set parametric; plot [t=-2:2] [] [] log10(10**t),(t<log10(1/(0.2))? 0:-90)
