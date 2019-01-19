/*
  Template for exercise 2. All required constants and tft/sd/touchscreen
  initializations are here, as is an implementation of getRestaurant
  (the slow version) that should be similar to what is covered in the lecture.

  Use it freely as a starting point for exercise 2.
*/

#include <Arduino.h>
#include <Adafruit_GFX.h>
#include <Adafruit_ILI9341.h>
#include <SD.h>
#include <TouchScreen.h>



#define TFT_DC 9
#define TFT_CS 10
#define SD_CS 6
#define TFT_WIDTH  320
#define TFT_HEIGHT 240
// physical dimensions of the tft display (# of pixels)
#define DISPLAY_WIDTH  320
#define DISPLAY_HEIGHT 240

// touch screen pins, obtained from the documentaion
#define YP A2  // must be an analog pin, use "An" notation!
#define XM A3  // must be an analog pin, use "An" notation!
#define YM  5  // can be a digital pin
#define XP  4  // can be a digital pin

// dimensions of the part allocated to the map display
#define MAP_DISP_WIDTH (DISPLAY_WIDTH - 48)
#define MAP_DISP_HEIGHT DISPLAY_HEIGHT

#define REST_START_BLOCK 4000000
#define NUM_RESTAURANTS 1066

// calibration data for the touch screen, obtained from documentation
// the minimum/maximum possible readings from the touch point
#define TS_MINX 150
#define TS_MINY 120
#define TS_MAXX 920
#define TS_MAXY 940

// thresholds to determine if there was a touch
#define MINPRESSURE   10
#define MAXPRESSURE 1000

#define BACKCOLOR 0x841F 
#define CHARCOL 0xFFFF
#define CHARBACK 0x0000
#define RED 0xF800
#define GREEN 0x07E0
#define BLUE 0x001F
#define BLACK 0x0000
#define YELLOW 0xFFE0
#define WHITE 0xFFFF
Adafruit_ILI9341 tft = Adafruit_ILI9341(TFT_CS, TFT_DC);

// a multimeter reading says there are 300 ohms of resistance across the plate,
// so initialize with this to get more accurate readings
TouchScreen ts = TouchScreen(XP, YP, XM, YM, 300);

// different than SD
Sd2Card card;

struct restaurant {
  int32_t lat;
  int32_t lon;
  uint8_t rating; // from 0 to 10
  char name[55];
};

uint32_t blocknum = 0;  
restaurant restblock[8];  //declare restblock and blocknum as global variable

int processTouchScreen() {
  TSPoint touch = ts.getPoint();

  if (touch.z < MINPRESSURE || touch.z > MAXPRESSURE) {
    return 0;
  }                      
  

  int16_t screen_x = map(touch.y, TS_MINY, TS_MAXY, TFT_WIDTH-1, 0);
  int16_t screen_y = map(touch.x, TS_MINX, TS_MAXX, 0, TFT_HEIGHT-1);
  delay(200);
  Serial.print(screen_x);
  Serial.print(' ');
  Serial.print(screen_y);
  Serial.print(' ');
  Serial.println(touch.z);  
  //----------------------------------------------- the code above this line in this function is copied from the stuff from class
  if (screen_x >= 272 && screen_y <= 120){
    return 1;
  }                                         //this area is the button for running the slow version. If this area is been touched, return 1
  else if (screen_x>= 272 && screen_y >= 120){
    return 2;                                
  }                                         //this area is the button for running the fast version. If this button is been touched, return 2
  return 0;                 //return 0 and exit
  
}

void setup() {
  init();
  Serial.begin(9600);

  // tft display initialization
  tft.begin();
  tft.fillScreen(ILI9341_BLACK);
  tft.setRotation(3);
  tft.setTextSize(2);
  // SD card initialization for raw reads
  tft.setCursor(0, 0);
  tft.println("Recent SLOW run: ");
  tft.println("Not yet run");
  tft.println("SLOW run avg:");
  tft.println("Not yet run");
  tft.println("Recent Fast run: ");
  tft.println("Not yet run");
  tft.println("FAST run avg: ");
  tft.println("Not yet run");
  //------------------------------------------ the code above this line is to initialize the display and print some words
  
  tft.setCursor(290,24);
  tft.println("S");
  tft.setCursor(290,40);
  tft.println("L");
  tft.setCursor(290,56);
  tft.println("0");
  tft.setCursor(290,72);
  tft.println("W");
  tft.setCursor(290,144);
  tft.println("F");
  tft.setCursor(290,160);
  tft.println("A");
  tft.setCursor(290,176);
  tft.println("S");
  tft.setCursor(290,192);
  tft.println("T");         
  //-------------------------------------------------- this part is to display the words on the button."slow" and "fast"       
  tft.drawRect( 272,1,47,120, RED);
  tft.drawRect( 272,120,47,120, RED);
  //---------------------------------------------------this two lines are to draw the edge of buttons
  if (!card.init(SPI_HALF_SPEED, SD_CS)) {
    Serial.println("failed! Is the card inserted properly?");
    while (true) {}
  }
  else {
    Serial.println("OK!");
  }

}

// the implementation from class
void getRestaurant(int restIndex, restaurant* restPtr) {
  uint32_t blockNum = REST_START_BLOCK + restIndex/8;
  restaurant restBlock[8];
  
  while (!card.readBlock(blockNum, (uint8_t*) restBlock)) {
    Serial.println("Read block failed, trying again.");
  }

  *restPtr = restBlock[restIndex % 8];
}              // original slow version 

void getRestaurantFast(int restIndex, restaurant* restPtr) {
  
 
  
  if (restIndex/8 + REST_START_BLOCK != blocknum){   //restIndex/8 + REST_START_BLOCK calculate the block number of restaurant whose index is "restIndex"
                                                      //blocknum is a global vairable, if the given restaurant is not in the block which has been read,   
  blocknum = restIndex/8 + REST_START_BLOCK;          //reset blocknum to the blocknumber contain the restaurant
   
  while (!card.readBlock(blocknum, (uint8_t*) restblock)) {    //I think .readblock is read to read ablock, 512 byte of data and stoe it
    Serial.println("Read block failed, trying again.");
  }
  
  }
  *restPtr = restblock[restIndex % 8];

}


void draw_black(uint16_t x0, uint16_t y0, uint16_t w, uint16_t h, uint16_t color){
  tft.drawRect(x0,y0,w,h,color);
  tft.fillRect(x0,y0,w,h,color);     //this function is to draw a square of black
}

int slow_time(){
  int time = millis(); // get the system time
  restaurant rest;        //declare rest
  for (int i = 0;i<NUM_RESTAURANTS-1;i++){
    getRestaurant(i,&rest);            //get the information of all the restaurant informtaion
  }
  time = millis() - time;  // calculate the time of getting all the restaurant information and return it
  return time;
}
int fast_time(){
  int time = millis();
  restaurant rest;
  for (int i =0; i<NUM_RESTAURANTS-1;i++){
    getRestaurantFast(i,&rest);          //the same as slow_time, but call getRestaurantFast this time
  }
  time = millis() - time;
  return time;
}




int main() {
  setup();
  int i1 = 0;      // count how many times getRestaurant has been called
  int total_slow = 0;    //the total time consumed by getRestaurantFast 
  int i2 = 0;     //count how many times getRestaurantFast  has been called
  int tota_fast = 0;   //the total time consumed by getRestaurantFast 
  
  while(true){
    if (processTouchScreen()==1){
      i1 += 1;
      tft.setTextSize(2);     
      tft.setCursor(0,16);
      draw_black(0,16,200,16,BLACK);
      draw_black(0,48,200,16,BLACK); //draw black to cover "not yet run"
      int recent1 = slow_time();     // get the runtime
      total_slow += recent1;             
      tft.println(recent1);           //print runtime 
      tft.setCursor(0,48);           
      tft.println(total_slow/i1);       //print the average runtime
    }
    else if (processTouchScreen()== 2)
    { 
      i2 += 1;
      tft.setTextSize(2);
      tft.setCursor(0,80);
      draw_black(0,80,200,16,BLACK);
      draw_black(0,112,200,16,BLACK);  //draw black to cover "not yet run"
      int recent2 = fast_time();        // get run time
      tota_fast += recent2; 
      tft.println(recent2);
      tft.setCursor(0,112);
      tft.println(tota_fast/i2);     //print average runtime
      
    }
    

  }
  
  Serial.end();
  return 0;
}
