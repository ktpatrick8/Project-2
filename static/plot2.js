console.log(window.location.pathname)

function buildMetadata(sample) {
    d3.json("/year2016").then((data) => {
        var metadata = data.Countries;
        var resultArray = metadata.filter(sampleObj => sampleObj.Name == sample);
        var result = resultArray[0];
        console.log(resultArray)
        // Use d3 to select `#sample-metadata`
        var metaData = d3.select("#sample-metadata");
      
        //clear any existing metadata
        metaData.html("");
      
        Object.entries(result).forEach(([key, value]) => {
        metaData.append("h5").text(`${key.toUpperCase()}: ${value}`);
        });
        });
      }

function init() {
var selector = d3.select('#selDataset');

d3.json('/happiness').then((data) => {
    var names = data.Countries;

    names.forEach((sample) => {
    selector.append("option")
        .text(sample)
        .property("value", sample);
    });
    var initSample = names[0];
    buildCharts(initSample);
    buildMetadata(initSample);
});
};

init();

function buildCharts(sample){
    d3.json("/year2016").then((data) => {
        var samples = data.Countries;
        var resultArray = samples.filter(sampleObj => sampleObj.Name == sample);
        var result = resultArray[0];
        values = []
        labels = []

        Object.entries(result).forEach(([key, value]) => {
            values.push(value)
            labels.push(key)
            });
            
        values.splice(5,3)
        labels.splice(5,3)
        console.log(values)
        console.log(labels)

        var pieData = [
            {  values: values,
                labels: labels,
                type: 'pie'

            }
        ];

        var layout = {
            margin: { t: 30, l: 150 }
          };

    // Building charts
    Plotly.newPlot("bar", pieData, layout);
    }   

)};


function optionChanged(option) {
    // Fetch new data each time a new sample is selected
    buildCharts(option);
    buildMetadata(option);
    functiongetRandomColor();
};

// function getRandomColor() {
//     var letters = '0123456789ABCDEF';
//     var color = '#';
//     for (var i = 0; i < 6; i++) {
//       color += letters[Math.floor(Math.random() * 16)];
//     }
//     return color;
//   }
  
//   data = '["Happ Cat 1","Hap Cat 2","Hap Cat 3","Hap Cat 4","Hap Cat 5","Hap Cat 6"," Hap Cat 7","Hap Cat 8","Hap Cat 9","Hap Cat 10"]';
//   var chart = new Chart(document.getElementById("pie"), {
//     type: 'pie',
//     data: {
//       labels: JSON.parse(data),
//       datasets: [{
//         label: "Anzahl Asservate",
//         backgroundColor: [getRandomColor(), getRandomColor(), getRandomColor(), getRandomColor(), getRandomColor(), getRandomColor(), getRandomColor(), getRandomColor(), getRandomColor(), getRandomColor()],
//         data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
//       }]
//     },
//     options: {
//       title: {
//         display: true,
//         text: 'Kategorien-Verteilung der Asservate'
//       }
//     }
//   });