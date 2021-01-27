console.log(window.location.pathname)
const url = "/year2015"
// d3.json(url).then((data) => {
//     // function filter10(happy) {
//     //     return happy.Rank < 11;
//     // }
//     // var top10happy = data.filter(filter10);
//     var countries = data.Name
//     console.log(countries);
// });
// if (window.location.pathname === "/") {
//     d3
//       .json("/year2015")
//       .then(data => {
//         const dataset = data.Countries[0];
//         console.log(dataset)
//       });
//     }
// }

function buildMetadata(sample) {
    d3.json("/year2016").then((data) => {
        var metadata = data.Countries;
        var resultArray = metadata.filter(sampleObj => sampleObj.Name == sample);
        var result = resultArray[0];
      
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
    // buildCharts(initSample);
    buildMetadata(initSample);
});
};

init();

function optionChanged(option) {
    // Fetch new data each time a new sample is selected
    buildCharts(option);
    buildMetadata(option);
  }