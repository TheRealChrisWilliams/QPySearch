# QPySearch
QPySearch is a tool that allows users to search for question papers on the Manipal Institute of Technology (MIT) library portal. The tool is built using Python, Selenium, and Tkinter. The file scrap.py contains the original scraper from Skyrptonyte's MITExamScrapper. All other code is built on top of it.

## How to Use
Clone or download the repository to your local machine.

Install the necessary dependencies by running pip install -r requirements.txt.

Run the script using python qpysearch.py.

A window will open up, enter the subject name or subject code in the text field and press the submit button.

The program will use Selenium to navigate the MIT library portal and search for question papers related to the subject entered.

The links to the question papers will be displayed in the text box at the bottom of the window.

Click on the link to open the question paper in a new tab.

Close the application when finished.

## Features
* Easy to use GUI interface
* Searches through all pages of the MIT library portal
* Extracts all links to question papers and displays them in the application
* Can search for question papers of a specific year
* Multi-threading implemented to keep the UI responsive
