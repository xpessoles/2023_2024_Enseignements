set table "gnuplot/Cy_01_ModelisationSystemes/7.table"; set format "%.5f"
set samples 50.0; set parametric; plot [t=-2:2] [] [] log10(10**t),20*log10(abs(20/sqrt(1+(0.2*10**t)**2)))
