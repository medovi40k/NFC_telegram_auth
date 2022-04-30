from flask import Flask
import keyboard
import time
app = Flask("")


  
@app.route("/", methods=['GET', 'POST'])
def slash():
	keyboard.write('password')
	time.sleep(0.2)
	keyboard.press_and_release('enter')
	return "Your bot is alive!"

	
def run():
	app.run(host="0.0.0.0", port=8080)
	
if (__name__=="__main__"):
  run()