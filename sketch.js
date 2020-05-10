var XScreenSize=720;var yScreenSize=480;var xCharacter=50;
var CharSize=30;var yVirus=300;var yChar=yVirus;var yM=7;
var yJ=yM;var VirusVelocity=10;var isScreenClear=true;
var xMove=XScreenSize;var jumpMag=8;var jumpLims=jumpMag;
var yInit=yChar-20;var yCC=yInit;var flag=0;var jumpGrowth=0.35;
var vVal=[0,10,20,30,40,50];var newV=0;

function setup() {
  createCanvas(720, 480);
}
function movement(xMove){
  if(xMove<=0)
     {
       xMove=XScreenSize;
       isScreenClear=true;
       newV=vVal[floor(random()*6)];
     }
  else
  {
    xMove-=10;
  }
  return(xMove);
}
function jump()
{
  //print("JumpLim= "+jumpLims);
    if(jumpLims===(-1*jumpMag))
    {  //print("THis goes true");
      jumpLims=jumpMag
        yCC=yInit;
        flag=0
    }
    else
    {
        yCC-=jumpLims*abs(jumpLims)*jumpGrowth;
        jumpLims=jumpLims-1;
        //print(jumpLims);
    }
  //print(jumpLim);
   // return(y,jumpLims,flag);
}


function draw() {
  print(vVal[floor(random()*5)]);
  background(0,200,255);
  fill(255,255,255);
  rect(xMove, yVirus-newV, 30, 30,30);
  fill(0,255,0);
  rect(0,yVirus+30,XScreenSize,yScreenSize);
  if (keyCode === UP_ARROW) {
    flag=1;
  }
  else if (keyCode === DOWN_ARROW) {
    //print("Down");
    flag=2;
  }
  else if(keyCode===RIGHT_ARROW)
  {
    flag=0;
    jumpLims=jumpMag;
    yCC=yInit;
  }
  keyCode=LEFT_ARROW;
  if(flag===1)
  {

    jump();
    //print(yCC);
    fill(230,160,200);
    rect(xCharacter,yCC-30,CharSize,CharSize+30);
  }
  else if(flag===2)
  {
    fill(230,160,200);
    rect(xCharacter,yCC+30,CharSize,CharSize-10);
  }
  else
  {
    fill(230,160,200);
    rect(xCharacter,yCC-10,CharSize,CharSize+30);
  }

  xMove=movement(xMove);
}
