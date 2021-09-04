
void setup()
{
  size(800,600);
}

void draw()
{
  background(128);
  float p1x = 100;
  float p1y = 100;
  float p2x = 90;
  float p2y = 250;
  float p3x = mouseX;
  float p3y = mouseY;
  float p4x = 700;
  float p4y = 100;
  beginShape();
  vertex(p1x, p1y);
  for(float t = 0; t <= 1; t += 0.01)
  {
    float ax = p1x + t*(p2x-p1x);
    float bx = p2x + t*(p3x-p2x);
    float cx = p3x + t*(p4x-p3x);
    
    float dx = ax + t*(bx-ax);
    float ex = bx + t*(cx-bx);
    float fx = dx + t*(ex-dx);
    
    float ay = p1y + t*(p2y-p1y);
    float by = p2y + t*(p3y-p2y);
    float cy = p3y + t*(p4y-p3y);
    
    float dy = ay + t*(by-ay);
    float ey = by + t*(cy-by);
    float fy = dy + t*(ey-dy);
    
    vertex(fx,fy);  
  }
  vertex(p4x, p4y);
  endShape(CLOSE);
}
