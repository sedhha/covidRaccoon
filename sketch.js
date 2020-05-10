var XScreenSize=720;var yScreenSize=480;var xCharacter=50;
var CharSize=30;var yVirus=300;var yChar=yVirus;var yM=7;
var yJ=yM;var VirusVelocity=10;var isScreenClear=true;
var xMove=XScreenSize;var jumpMag=7;var jumpLim=jumpMag;
var yInit=yChar-20;var yCC=yInit;var flag=0;var jumpGrowth=0.35;

function setup() {
  createCanvas(720, 480);
}
function movement(xMove){
  if(xMove<=0)
     {
       xMove=XScreenSize;
       isScreenClear=true;
     }
  else
  {
    xMove-=10;
  }
  return(xMove);
}
function jump(y,jumpLims,flag)
{
  //print("JumpLim= "+jumpLims);
    if(jumpLims===(-1*jumpMag))
    {  print("THis goes true");
      jumpLims=jumpMag
        y=yInit;
        flag=0
    }
    else
    {
        y-=jumpLims*abs(jumpLim)*jumpGrowth;
        jumpLims=jumpLims-1;
        print(jumpLims);
    }
  //print(jumpLim);
    return(y,jumpLims,flag);
}


function draw() {
  background(0,200,255);
  fill(255,255,255);
  rect(xMove, yVirus, 30, 30,30);
  fill(0,255,0);
  rect(0,yVirus+30,XScreenSize,yScreenSize);
  if (keyCode === UP_ARROW) {
    flag=1;
  }
  else if (keyCode === DOWN_ARROW) {
    print("Down");
  }
  keyCode=LEFT_ARROW;
  if(flag===1)
  {
    yCC,jumpLim,flag=jump(yCC,jumpLim,flag);
    //print(yCC);
    fill(230,160,200);
    rect(xCharacter,yCC-20,CharSize,CharSize+20);
  }
  else
  {
    fill(230,160,200);
    rect(xCharacter,yCC,CharSize,CharSize+20);
  }

  xMove=movement(xMove);
}
