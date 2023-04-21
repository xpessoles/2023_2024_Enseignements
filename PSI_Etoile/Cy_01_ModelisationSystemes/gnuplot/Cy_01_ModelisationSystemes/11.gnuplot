set table "gnuplot/Cy_01_ModelisationSystemes/11.table"; set format "%.5f"
set samples 150.0; set parametric; plot [t=-2:2] [] [] log10(10**t),(t<log10(.9)?20*log10(10):+20*log10(10)+40*log10(.9)-40*log10(10**t))
