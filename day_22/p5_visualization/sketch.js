// Sources:

function windowResized() {
  setup();
}

function setup() {
  const totalHeight = window.innerHeight;
  const totalWidth = window.innerWidth;

  const navBarHeight = 0;
  const detailBarHeight = 0;

  canvasHeight = totalHeight-navBarHeight-detailBarHeight;
  canvasWidth = totalWidth;

  const canvas = createCanvas(canvasWidth, canvasHeight, WEBGL);
  canvas.parent('canvasContainer');

  background(0);
  cursor('grab');
	camera(175, -175, 200, 0, 0, 0, 0, 1, 0);
}

function draw() {
  // Enable orbit control
	orbitControl();

	//console.log(frameRate());
	if (frameRate() < 5){
		resetSketch();
	}


  background(200);
  // rotateX(frameCount * 0.01);
  // rotateY(frameCount * 0.01);
  plane();
  box();
}

// function clearBG() {
//   background(0);
// }


