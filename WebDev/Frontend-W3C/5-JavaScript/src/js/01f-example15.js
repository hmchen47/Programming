var ttt = functionPlot({
  target: '#quadratic',
  data: [{
    fn: 'x^2', 
    color: 'red',
    derivative: {
      fn: '2 * x',
      color: 'green',
      updateOnMouseMove: true
    }
  }],
  grid: true,
  yAxis: {domain: [0, 1]},
  xAxis: {domain: [0, 1]}
});

ttt.root.width="200px";
ttt.root.height="200px";

functionPlot({
  target: '#sin',
  data: [{
    fn: 'sin(x)', 
    color: 'blue', 
    range: [-1, 8], 
    closed: true
  }],
  tip: {
      xLine: true,
      yLine: true
  },
  yAxis: {domain: [-2, 3]},
  xAxis: {domain: [-2, 9]},
});

functionPlot({
  target: '#multiple',
  data: [
    {fn: 'x*x', color: 'red'},
    {fn: '3*x', color: 'green'},
    {fn: 'cos(x)', 
     color: 'blue', 
     range: [3, 6],
     closed: true
    },
    {fn: 'cos(x)', 
     color: 'blue' 
    },
    {fn: '-3*x^2 + x^2', 
     nSamples: 150, 
     graphType: 'scatter'}
  ]
});
