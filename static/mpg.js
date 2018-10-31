$(document).ready(function(){
  console.log('document is ready')

  $('#inference').click(async function(){
    console.log('button was clicked')
    const cylinders = parseFloat($('#cylinders').val());
    const horsepower = parseFloat($('#horsepower').val());
    const weight = parseFloat($('#weight').val());
    const data = {
      cylinders,
      horsepower,
      weight
    }
    console.log(data)
    const response = await $.ajax('/inference',{
      data: JSON.stringify(data),
      method: "post",
      contentType: "application/json"
    })
    console.log(response)
    $('#mpg').val(response.prediction)
  })

  $('#scatter-plot').click(async function(){
    console.log('scatter button was clicked')
    const response = await $.ajax('/plot')
    console.log(response)
    const mpg = response.map(a => a[0])
    const weight = response.map(a => a[1])
    console.log(mpg)

    //Create the trace
    const trace = [{
      x:weight,
      y:mpg,
      mode:"markers",
      type:"scatter"
    }]

    //Create the layout
    const layout = {
      xaxis:{
        title:'Weight'
      },
      yaxis:{
        title:"MPG"
      },
      title: "Scatter MPG vs. Weight",
      width:700,
      height:300
    }
  })
})
