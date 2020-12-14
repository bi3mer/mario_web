const resolution = 50;
const width = 400;
const height = 400;
const widthAdder = width / resolution;
const heightAdder = height / resolution;

var canvas = document.getElementById("canvas");


$('#canvas').click((e) => {
  const rect = canvas.getBoundingClientRect()
  const x = event.clientX - rect.left;
  const y = Math.abs(event.clientY - rect.top - height);

  gridX = Math.ceil(x / widthAdder) - 1;
  gridY = Math.ceil(y / heightAdder) - 1;
  console.log(gridX, gridY);
});

function buildGrid() {
  var ctx = canvas.getContext("2d");
  
  let w = 0;
  let h = 0; 
  let nextW = widthAdder;
  let nextH = heightAdder;

  for(let y = 0; y < resolution; ++y) {
    for(let x = 0; x < resolution; ++x) {
      const randomColor = Math.floor(Math.random()*16777215).toString(16);
      ctx.fillStyle = `#${randomColor}`;
      ctx.fillRect(w, h, nextW, nextH);
      
      w = nextW;
      nextW += widthAdder
    }
    
    w = 0;
    nextW = widthAdder;
    h = nextH;
    nextH += widthAdder
  }
}


function main() {
  buildGrid();
  // get data file and update grid elements and add call on click to 
  // gridButtonPress
}

main();