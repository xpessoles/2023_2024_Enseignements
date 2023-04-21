set table "gnuplot/Cy_01_ModelisationSystemes/12.table"; set format "%.5f"
set samples 150.0; set parametric; plot [t=-2:2] [] [] log10(10**t),20*log10(abs(10/sqrt((1-(10**t/.9)**2)**2+(2*0.2*(10**t/.9))**2)))
