// Zip xaxis data, yaxis data, and labels into one JSON object
function zipxy(xaxis,yaxis,zvals) {
    if (xaxis.length !== yaxis.length) return false;
    const obj = [];
    for (let i = 0; i < xaxis.length; i++) {
      obj.push({x: xaxis[i], y: yaxis[i], name: zvals[i]});
    }
    return obj;
  }
// Chart clash data
function graph(xaxis, yaxis, zvals) {
    let data = zipxy(xaxis, yaxis, zvals);
    let ctx = document.getElementById('myChart');
  
    // Create data
    const datas = {
      datasets: [{
        label: 'League of Legends',
        data: data,
        backgroundColor: 'rgb(255, 99, 132)',
        borderColor: 'rgb(255, 99, 132)',
        fill: false,
        trendlineLinear: {
          style: "rgb(43 ,66 ,255, 0.3)",
          lineStyle: "solid",
          width: 3
        }
      }],
    };
  
    // Plugin for labels on scatter points
    const scatterDataLabels = {
      id: 'scatterDataLabels',
      afterDatasetsDraw(chart,args,options) {
        const { ctx } = chart;
        ctx.save();
        ctx.font = '12px sans-serif';
        for (let i = 0; i < chart.config.data.datasets[0].data.length; i++) {
          const textWidth = ctx.measureText(chart.config.data.datasets[0].data[i].name).width;
          ctx.fillText(chart.config.data.datasets[0].data[i].name, chart.
            getDatasetMeta(0).data[i].x - (textWidth/2), chart.getDatasetMeta(0).data[i].y - 10)
        }
      }
    }
  
    // config
    const config = {
      type: 'scatter',
      data: datas,
      options: {
        radius: 5,
        hoverRadius: 7,
        scales: {
          x: {
            title: {
              display: true,
              text: 'Clash games played'
            }
          },
          y: {
            title: {
              display: true,
              text: 'Clash games won'
            }
          }
        }
      },
      plugins: [scatterDataLabels]
    };
  
    const myChart = new Chart(ctx, config);
  }
  