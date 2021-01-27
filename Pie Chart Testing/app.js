function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }
  
  data = '["Generosity","Gov Trust","Freedom","Health","Family"," Economy"]';
  var chart = new Chart(document.getElementById("pie"), {
    type: 'pie',
    data: {
      labels: JSON.parse(data),
      datasets: [{
        label: "Some Happiness Data",
        backgroundColor: [getRandomColor(), getRandomColor(), getRandomColor(), getRandomColor(), getRandomColor(), getRandomColor(), getRandomColor(), getRandomColor(), getRandomColor(), getRandomColor()],
        data: [1, 2, 3, 4, 5, 6],
      }]
    },
    options: {
      title: {
        display: true,
        text: 'Happiness Category Data'
      }
    }
  });