set table "gnuplot/Cy_01_ModelisationSystemes/6.table"; set format "%.5f"
set samples 100.0; set parametric; plot [t=-2:2] [] [] log10(10**t),(t<log10(1/(0.2))?20*log10(20):+20*log10(20/(0.2))-20*log10(10**t))
