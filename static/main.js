const resolution = 50;
const width = 400;
const height = 400;
const widthAdder = width / resolution;
const heightAdder = height / resolution;
let data;

const canvas = document.getElementById("canvas");
const context = canvas.getContext("2d");

let recentMap = null;

$('#canvas').click((e) => {
  const rect = canvas.getBoundingClientRect()
  const x = e.clientX - rect.left;
  const y = Math.abs(e.clientY - rect.top - height);

  const linearity = Math.ceil(x / widthAdder) - 1;
  const leniency = Math.ceil(y / heightAdder) - 1;

  let found = -1;
  for(let i = 0; i < data.length; ++i) {
    const row = data[i];
    if(row[0] == linearity && row[1] == leniency) {
      found = i;
      break;
    }
  }

  if(found == -1) {
    $('#map').text(`No corresponding map for linearity bin = ${linearity}, leniency bin = ${leniency}`);
  } else {
    console.log('here');
    console.log(recentMap);
    if(recentMap === null) {
      $.get(`/get-map/${found}`, (map) => { 
        $('#map').text(map);
      });
    } else {
      $.get(`/get-combo/${recentMap}/${found}`, (map) => { 
        $('#map').text(map);
      });
    }

    recentMap = found;
  }
});

function buildGrid() {
  $.get( "/get-data/data", (d) => {
    // draw squares
    data = JSON.parse(d);
    data.forEach((row) => {
      const linearity = row[0];
      const leniency = row[1];
      const percentPlayable = row[2]

      context.fillStyle = `rgb(20, ${255 * percentPlayable}, 220)`;
      context.fillRect(
        linearity * widthAdder, 
        height - (leniency * heightAdder), 
        widthAdder, 
        heightAdder);
    });

    // draw grid
    context.fillStyle = `rgb(0,0,0)`;
    context.fillStyle = `rgb(100,100,100)`;
    let w = 0;
    let h = 0;
    for(let i = 0; i < resolution; ++i) {
      context.fillRect(w, 0, 1, height);
      context.fillRect(0, h, width, 1);

      w += widthAdder;
      h += heightAdder;
    }
  });
}

buildGrid();