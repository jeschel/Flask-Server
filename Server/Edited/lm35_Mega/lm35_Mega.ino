 
float tempF;
int reading;
int tempPin = A0;

void setup()
{
  pinMode(13,OUTPUT);
  pinMode(10,OUTPUT);
  analogReference(INTERNAL1V1);
  Serial.begin(9600);
  Serial1.begin(9600);
}

void loop()
{ 
  digitalWrite(13,0);
  if(Serial.readString() == "H")
  {
   digitalWrite(10,1);
  }
  if(Serial.readString() == "L")
  {
    digitalWrite(10,0);
  }
  
 reading = analogRead(tempPin);
 tempF = reading / 10.1;
 Serial1.print(tempF);
 Serial1.print(" C\n");
 
}

