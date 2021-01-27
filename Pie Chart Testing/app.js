function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }
  
  data = '["Happ Cat 1","Hap Cat 2","Hap Cat 3","Hap Cat 4","Hap Cat 5","Hap Cat 6"," Hap Cat 7","Hap Cat 8","Hap Cat 9","Hap Cat 10"]';
  var chart = new Chart(document.getElementById("pie"), {
    type: 'pie',
    data: {
      labels: JSON.parse(data),
      datasets: [{
        label: "Some Happiness Data",
        backgroundColor: [getRandomColor(), getRandomColor(), getRandomColor(), getRandomColor(), getRandomColor(), getRandomColor(), getRandomColor(), getRandomColor(), getRandomColor(), getRandomColor()],
        data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      }]
    },
    options: {
      title: {
        display: true,
        text: 'Happiness Category Data'
      }
    }
  });