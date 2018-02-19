set term pngcairo size 1000,1000
set output "regiones.png"
set size square
set key off
set xrange [-.1:1.1]
set yrange [-.1:1.1]
set xlabel "Longitud (m)"
set ylabel "Longitud (m)"
set style fill  transparent solid 0.35 border
plot "nodos.csv" w points palette pt 7 ps 4, "regiones.csv" u 1:2:3 w circle 
quit()
