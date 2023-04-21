set table "gnuplot/Cy_01_ModelisationSystemes/10.table"; set format "%.5f"
set samples 50.0; set parametric; plot [t=-2:2] [] [] log10(10**t),-180/3.1415957*atan(0.2*10**t)
