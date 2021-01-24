var ttt = functionPlot({
  target: '#myFunction',
  data: [{
    fn: 'sin(x^2)', 
    color: 'red'
 }],
  grid: true,
  yAxis: {domain: [-1, 1]},
  xAxis: {domain: [0, 2*Math.PI]},
});

