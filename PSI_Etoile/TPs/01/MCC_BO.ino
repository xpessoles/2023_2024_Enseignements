#define PWM1 9 // ou PIN 9 // 6
#define PWM2 10 // ou 10  9 //10

#define VOIE_A 2 //
#define VOIE_B 3 //

float uc;
int pwm1;
int pwm2;

volatile int cpt = 0;

void setup() {
  // Setup du PWM
  pinMode(PWM1, OUTPUT);
  pinMode(PWM2, OUTPUT);
  // Setup du codeur
  pinMode(VOIE_A,INPUT); 
  pinMode(VOIE_B,INPUT);  
  attachInterrupt(digitalPinToInterrupt(VOIE_A),codeur,CHANGE);
 // Ouverture du port série
  Serial.begin(9600); 
}

void loop() {
  for (int t=0; t<500; t++)
   {
     Serial.print(cpt);Serial.print(",");Serial.print(cpt);Serial.println();
     moteur(0);
     delay(1);
   }

  for (int t=0; t<500; t++)
   {
     Serial.print(cpt);Serial.print(",");Serial.print(cpt);Serial.println();
     moteur(-100);
     delay(1);
   }

  for (int t=0; t<500; t++)
   {
     Serial.print(cpt);Serial.print(",");Serial.print(cpt);Serial.println();
     moteur(100);
     delay(1);
   }
   
  }

void moteur(float x){
  // Commande du moteur (commande comprise entre -255 et 255)
   if (x>0){
    pwm1 = 255;
    pwm2 = 255 - x;
  } else {
    pwm1 = 255+x ;
    pwm2 = 255 ;
  }
  analogWrite(PWM1,pwm1);
  analogWrite(PWM2,pwm2);
  }

void codeur(){
  int a = digitalRead(VOIE_A);
  int b = digitalRead(VOIE_B);
  if(a==b){
    cpt++;
  }
  else{
    cpt--;
  }
}
