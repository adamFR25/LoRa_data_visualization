#include <TinyGPS++.h>
#include <RH_RF95.h>

#define RFM95_CS 10
#define RFM95_RST 9
#define RFM95_INT 2

// Change to 434.0 or other frequency, must match RX's freq!
#define RF95_FREQ 920.0

// Singleton instance of the radio driver
TinyGPSPlus gps;
RH_RF95 rf95;

char gps4 [700];
float lintang[500];
float bujur[500];
float a, b, c;
int counter = 0;
double millisawal, millisupdate, totalmillis, m1;
String aa, bb, GPS, cnt, Angka, lins, linf, longs, longf;

void setup()
{
  //millisawal = millis() * 0.000277778;
  pinMode(RFM95_RST, OUTPUT);
  digitalWrite(RFM95_RST, HIGH);
  Serial3.begin(9600);
  Serial.begin(115200); // connect serial
  Serial.println("The GPS Received Signal:");
  while (!Serial);
  Serial.println("Arduino LoRa TX Test!");
  Serial.println("GPS Mulai");

  // manual reset
  digitalWrite(RFM95_RST, LOW);
  delay(10);
  digitalWrite(RFM95_RST, HIGH);
  delay(10);

  while (!rf95.init()) {
    Serial.println("LoRa radio init failed");
    while (1);
  }
  Serial.println("LoRa radio init OK!");

  // Defaults after init are 434.0MHz, modulation GFSK_Rb250Fd250, +13dbM
  if (!rf95.setFrequency(RF95_FREQ)) {
    Serial.println("setFrequency failed");
    while (1);
  }

  // Defaults after init are 434.0MHz, 13dBm, Bw = 125 kHz, Cr = 4/5, Sf = 128chips/symbol, CRC on

  // The default transmitter power is 13dBm, using PA_BOOST.
  // If you are using RFM95/96/97/98 modules which uses the PA_BOOST transmitter pin, then
  // you can set transmitter powers from 5 to 23 dBm:
  //
  //  rf95.setSpreadingFactor(7);
  //  rf95.setSignalBandwidth(125000);
  //  rf95.setCodingRate4(5);
  //  rf95.setSyncWord(0x34);
}

void loop()
{
  while (Serial3.available()) {
    if (gps.encode(Serial3.read())) // encode gps data
    {
      a = gps.location.lat();
      b = gps.location.lng();
      aa = String(a, 6);
      bb = String(b, 6);
      Serial.print(totalmillis);
      Serial.print("Kirim Data : ");
      Serial.print(aa);
      Serial.print (",");
      Serial.println(bb);
      cnt = String(counter);
      GPS = "02" + aa + "," + bb ;
      GPS.toCharArray(gps4, 100);///////////KONVERSI STRING KE CHAR ARRAY
      rf95.send(gps4, sizeof(gps4));////////////KIIRM DATA KE RX
      delay(1000);
    }
  }
}
