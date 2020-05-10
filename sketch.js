function setup() {
  createCanvas(640, 480);
  character = loadImage('assets/character.png');

}

function draw() {
  background(0,0,0);
  image(character, 100, 100);
}
