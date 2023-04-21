set table "gnuplot/Cy_01_ModelisationSystemes/13.table"; set format "%.5f"
set samples 100.0; set parametric; plot [t=-2:2] [] [] log10(10**t),180/3.1415957*(atan((.9**2-(10**t)**2)/(2*0.2*.9*10**t))-3.1415957/2)
