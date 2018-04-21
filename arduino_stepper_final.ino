int Distance = 0;
int inByte;
int i;
int a1;
int b;
int a;
int Distance1 = 0;
void vaccum(int dist, int dir)
{
  Serial.println("Chamber 2");
  for (Distance1 = 0 ; Distance1 < dist ; Distance1++)
  {
    digitalWrite(8, dir);//2
    digitalWrite(9, HIGH);//3
    delay(0.01);
    digitalWrite(9 , LOW);//3
    delay(0.01);
    Serial.println(Distance1);
  }
}
void setup()
{
  // Record the number of steps we've taken void setup() {

  pinMode(8, OUTPUT);//direction of roller
  pinMode(9, OUTPUT);//step of roller
  pinMode(2, OUTPUT);//direction of roller
  pinMode(3, OUTPUT);//direction of roller
  digitalWrite(8, LOW);
  digitalWrite(9, LOW);
  digitalWrite(2, LOW);
  digitalWrite(3, LOW);
  Serial.begin(9600);
}
int code = 0;
int flag = 0;
void loop()
{
  int a;
    if (flag) {
        //Serial.println(code);
        if (code == 1)
        {
         Serial.println("Chamber 1");
          for (Distance = 0 ; Distance < 140; Distance++)
          {
            digitalWrite(9, HIGH);
            delay(0.01);
            digitalWrite(9, LOW);
            delay(0.01);
            Serial.println(Distance);

          }
        } else {
          int direct = code % 10;
          code = code / 10;
          vaccum(code, direct);
          code = 0;
        }
         code = 0;
          flag = 0;
      } 
  if (Serial.available() > 0)
  {

    inByte = Serial.read();
    if (inByte != 13 && inByte != 10) {
      if (inByte == 92) {
          flag = 1;
        } else {
          int val = inByte - 48;
          code = code * 10 + val;
        }
    }
  }
}


