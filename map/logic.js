
// Create Map
var myMap = L.map("map", {
  center: [48.864716, 2.349014],
  zoom: 2.5
});

// Define Base Layer Map Tiles
L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>IWM DataViz</a></strong>",
  tileSize: 512,
  maxZoom: 18,
  zoomOffset: -1,
  id: "mapbox/streets-v11",
  accessToken: API_KEY
}).addTo(myMap);

// File Link to geojson data
var link = "data/custom.geo.json";


// Function that colors the countries based on their respective 'Happiness' scores
function chooseColor(name) {
  countryNames=['Costa Rica',	 'Dominican Rep.',	 'Guatemala',	 'Honduras',	 'Haiti',	 'Jamaica',	 'Mexico',	 'Nicaragua',	 'Panama',	 'United States',	 'El Salvador',	 'Canada',	 'Trinidad and Tobago',	 'Bolivia',	 'Ecuador',	 'Colombia',	 'Argentina',	 'Brazil',	 'Peru',	 'Uruguay',	 'Paraguay',	 'Suriname',	 'Azerbaijan',	 'United Arab Emirates',	 'Afghanistan',	 'Armenia',	 'Venezuela',	 'Bahrain',	 'Bangladesh',	 'Bhutan',	 'Chile',	 'Cyprus',	 'Georgia',	 'Hong Kong',	 'China',	 'Israel',	 'Jordan',	 'Iran',	 'India',	 'Iraq',	 'Indonesia',	 'Japan',	 'Korea',	 'Kazakhstan',	 'Kyrgyzstan',	 'Cambodia',	 'Kuwait',	 'Lao PDR',	 'Sri Lanka',	 'Lebanon',	 'Mongolia',	 'Oman',	 'Myanmar',	 'Malaysia',	 'Nepal',	 'Pakistan',	 'Philippines',	 'Saudi Arabia',	 'Qatar',	 'Singapore',	 'Syria',	 'Thailand',	 'Turkmenistan',	 'Taiwan',	 'Uzbekistan',	 'Tajikistan',	 'Turkey',	 'Vietnam',	 'Burundi',	 'Yemen',	 'Angola',	 'Benin',	 'Burkina Faso',	 'Central African Rep.',	 "Côte d'Ivoire",	 'Botswana',	 'Cameroon',	 'Dem. Rep. Congo',	 'Djibouti',	 'Comoros',	 'Ethiopia',	 'Algeria',	 'Gabon',	 'Egypt',	 'Ghana',	 'Guinea',	 'Kenya',	 'Liberia',	 'Libya',	 'Lesotho',	 'Morocco',	 'Madagascar',	 'Mozambique',	 'Mali',	 'Niger',	 'Mauritania',	 'Malawi',	 'Nigeria',	 'Rwanda',	 'Sudan',	 'Sierra Leone',	 'Somaliland',	 'Togo',	 'Swaziland',	 'Senegal',	 'Chad',	 'Tanzania',	 'Tunisia',	 'Zimbabwe',	 'Uganda',	 'South Africa',	 'Albania',	 'Zambia',	 'Austria',	 'Bulgaria',	 'Belgium',	 'Czech Rep.',	 'Bosnia and Herz.',	 'Switzerland',	 'Belarus',	 'Denmark',	 'Germany',	 'Spain',	 'Estonia',	 'United Kingdom',	 'France',	 'Finland',	 'Hungary',	 'Croatia',	 'Greece',	 'Ireland',	 'Kosovo',	 'Iceland',	 'Luxembourg',	 'Italy',	 'Latvia',	 'Lithuania',	 'Malta',	 'Macedonia',	 'Moldova',	 'Poland',	 'Portugal',	 'Slovakia',	 'Norway',	 'Serbia',	 'Romania',	 'Montenegro',	 'Netherlands',	 'Slovenia',	 'Ukraine',	 'Sweden',	 'Russia',	 'Australia',	 'New Zealand']
	happiness = [7.226,4.885,6.123,4.788,4.518,5.709,7.187,5.828,6.786,7.119,6.13,7.427,6.168,5.89,5.975,6.477,6.574,6.983,5.824,6.485,5.878,6.269,5.212,6.901,3.575,4.35,6.81,5.96,4.694,5.253,6.67,5.689,4.297,5.474,5.14,7.278,5.192,4.686,4.565,4.677,5.399,5.987,5.984,5.855,5.286,3.819,6.295,4.876,4.271,4.839,4.874,6.853,4.307,5.77,4.514,5.194,5.073,6.411,6.611,6.798,3.006,6.455,5.548,6.298,6.003,4.786,5.332,5.36,2.905,4.077,4.033,3.34,3.587,3.678,3.655,4.332,4.252,4.517,4.369,3.956,4.512,5.605,3.896,4.194,4.633,3.656,4.419,4.571,5.754,4.898,5.013,3.681,4.971,3.995,3.845,4.436,4.292,5.268,3.465,4.55,4.507,5.057,2.839,4.867,3.904,3.667,3.781,4.739,4.61,3.931,4.642,4.959,5.129,7.2,4.218,6.937,6.505,4.949,7.587,5.813,7.527,6.75,6.329,5.429,6.867,6.575,7.406,4.8,5.759,4.857,6.94,5.589,7.561,6.946,5.948,5.098,5.833,6.302,5.007,5.889,5.791,5.102,5.995,7.522,5.123,5.124,5.192,7.378,5.848,4.681,7.364,5.716,7.284,7.286];

	for (i=0;i<countryNames.length;i++){
		if (name==countryNames[i]){
			score=happiness[i];
			console.log(score);
			
		}
  }
  color=""
  console.log(score);
	if (score >=7.6) { color='#67001f'; }
    else if (score >=7) { color='#980043';}
    else if (score >=6.4) { color='#ce1256';}
		else if (score >=5.8) { color='#e7298a';}
    else if (score >=5.2) { color='#df65b0';}
		else if (score >=4.6) { color='#c994c7';}
		else if (score >=4) { color='#d4b9da';}
		else if (score >=3.4) { color='#e7e1ef';}
  else { color='#f7f4f9'; }
  return color;
}


// Function to create the country polygon layer
d3.json(link, function(data) {

  geoJson = L.geoJson(data, {
    
    style: function (feature) {
      console.log(feature.properties.name);
      return {
        color: "white",
        
        fillColor: chooseColor(feature.properties.name),
        fillOpacity: 0.7,
        weight: 1.5
      };
    },
    // Define the user interactivity functions for the map
    onEachFeature: function(feature, layer) {
      
      layer.on({
        // When the cursor is over the country make it darker in color
        mouseover: function(event) {
          layer = event.target;
          layer.setStyle({
            fillOpacity: 1
          });
        },
        // When the cursor leaves the country return it to its original color 
        mouseout: function(event) {
          geoJson.resetStyle(event.target);
        },
        // When user clicks on country  - zoom in and show country in full screen and display name and population
        click: function(event) {
          myMap.fitBounds(event.target.getBounds());
        }
      });
      
      layer.bindPopup("<h1>" + feature.properties.admin + "</h1> <hr> <h3>" + "Pop: " + feature.properties.pop_est +  "<br> Income Cat: " + feature.properties.income_grp +"</h3>");
    }
  }).addTo(myMap);

  // Set up the legend
  var legend = L.control({ position: "bottomright" });
  legend.onAdd = function() {
    var div = L.DomUtil.create("div", "info legend");
    var limits = [0, 3.4, 4, 4.6, 5.2, 5.8, 6.4, 7, 8];
    var colors = ["#f7f4f9","#e7e1ef","#d4b9da","#c994c7","#df65b0","#e7298a","#ce1256","#980043","#67001f"];
    var labels = [];

    // Add min & max
    var legendInfo = "<h1>Happiness Scores</h1>" +
      "<div class=\"labels\">" +
        "<div class=\"min\">" + limits[0] + "</div>" +
        "<div class=\"max\">" + limits[limits.length - 1] + "</div>" +
      "</div>";

    div.innerHTML = legendInfo;

    limits.forEach(function(limit, index) {
      labels.push("<li style=\"background-color: " + colors[index] + "\"></li>");
    });

    div.innerHTML += "<ul>" + labels.join("") + "</ul>";
    return div;
  };

  // Adding legend to the map
  legend.addTo(myMap);






});
