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
if (window.location.pathname === "/") {
    d3
      .json("/year2015")
      .then(data => {
        const dataset = data.Countries[0];
        console.log(dataset)
      });
    }