# Flask Template Rendering Demo
-
This repo serves as a demo for both rendering templates with Flask and for showing the  frontend > server > db > server > frontend chain of events.

## Running the App
Clone this repo, cd into the root directory of the repository, and in Terminal or Gitbash, run `python app.py`. This will start the development server. If you go to `localhost:5000` in your browser, you should see a blank window that says "Get All Stations" in the upper left hand corner.

## What this Tiny App is Meant to Demonstrate
When you click the link, it kicks off a chain of events. 
##### The Chain of Events
	index.html (frontend):
		The <a> tag on line 11 calls the 'get_all_stations' function in app.py
		
	app.py (server): 
		The get_all_stations() function queries the database for all stations
		
	hawaii.sqlite (db): 
		Provides the data requested to the server
		
	app.py (server): 
		Renders display_data.html, sending the provided data along with it
		
	display_data.html (frontend):
		Receives and displays the data provided by the render_template return statment in
		get_all_stations().
		

