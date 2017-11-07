var polyline = require('polyline');

// returns an array of lat, lon pairs
const myArray = polyline.decode('sifhFb_|iOvB~EzE~KhFtLbAdCl@nA|@zBsAr@}A~@gAx@{AtAaCfB}AlAsA|@p@`BV`@ZVhB|@d@Xt@n@z@l@K^Mj@_@|CE`@lAXSnB@VBLz@jBTX\P');
console.log(myArray)
// returns a string-encoded polyline
//polyline.encode([[38.5, -120.2], [40.7, -120.95], [43.252, -126.453]]);

// returns a string-encoded polyline from a GeoJSON LineString
//polyline.fromGeoJSON({ "type": "Feature",
//  "geometry": {
//    "type": "LineString",
//    "coordinates": [[-120.2, 38.5], [-120.95, 40.7], [-126.453, 43.252]]
//  },
//  "properties": {}
//});

require('fs').writeFile(

    './my.json',

    JSON.stringify(myArray),

    function (err) {
        if (err) {
            console.error('Crap happens');
        }
    }
);
