#### Maryam Seifeldin
#### SI 508 Final Project

#  `DEEP TUNES`

##### The program scrapes a list of the current best selling albums from Billboard, then gets their respective album covers from the iTunes API and runs them through the Deep Dream API then creates a collage of this art.

##### A sample of the output is located in the sample_output directory in this repository.

### To get a deep dream API key:
 * to to https://deepai.org/
 * register with your email and a password
 * confirm your email via the link sent to you (the email may take a few hours to receive)
 * if this takes too long, email me for my key

### Before you run this program, make sure you have the following packages installed:
 * requests (pip install requests)
 * bs4/BeautifulSoup (pip install beautifulsoup4)
 * PIL (pip install Pillow)

### If you're running on a Mac, make sure you have your python certificates installed:
 * go to Macintosh HD > Applications > Python3.6 folder (or whatever version of python you're using)
 * double click on "Install Certificates.command" file

### This project involves downloading some files to your machine. In the project_path.py file:
 * change the project_path variable to the file path from the Users level thru to the directory to which you downloaded this repository
 * if you're on a PC, change the slashes in the local_path variable to backslashes

### To run the main program after forking/cloning this repository:
* paste your API key into its designated variable in the secrets.py file
* run the file "runfile.py" with python in your terminal
* when the project is finished running, it should launch an image utility (i.e. Preview on Mac machines) on your machine to display the deep dream collage and list the albums that were used to make it
* if you don't happen to have an appropriate image utility on your machine and nothing launches, you can still access the output image by opening the dream.jpg file in the albumimages directory in this repository

### To run the test suite:
* run the file "runfile_tests.py" with python in your terminal
* the file should then output the test results


#### Base level requirements:
* At least two data sources used in total (APIs, pages to scrape, datasets you access): Billboard scraping, iTunes API , deep dream API
* Caching must be implemented and/or used for any data sourced from the internet, scraping or API(s): yes; caching_protocol.py, project_cache.json
* Process data from each source (e.g. accessing a dictionary of data from a service and saving the dictionary to a .json file without pulling data out of it or altering its format would NOT fulfill this processing requirement — you should pull pieces out of data, or alter its format, or perform some other form of computation / processing with code in some nature): using billboard info to pull album cover image URLs from iTunes API and downloading & saving the images; creating a collage from the saved images and saving it too; sending the collage through deep dream, taking the url response and downloading, saving, and showing the image from the url.
* Import and use functionality from at least one Python module that is not json, random, or requests : using PIL(Pillow) in main program and os module in test suite
* A test suite file containing at least 2 unittest.TestSuite subclasses and at least 10 test methods (beginning with test) which are non-trivial tests: yes; runfile_tests.py
* Running the project should produce a product that is the result of processing data (a new dataset and explanation, a visualization, a prototype of a useful interactive product, a game… could be anything): program creates a deep dream image collage
* Define at least 2 classes and create and use instance(s) of each of them: Album and AlbumImage classes
* Include in your repository an example of your output (e.g. a screenshot of a finished version, an example output file… whatever your project does generate, show us an actual example as well as describing it briefly in the README): in sample_output directory

#### Second level requirements:
* Scraping data that comes in HTML or XML form using BeautifulSoup: Billboard scraping
* Using a library in Python that we did not study in SI 508 or use in any assignment / project (this can include a library that you discussed in 1 section meeting only): using PIL(Pillow) in main program and os module in test suite
* Complex object-oriented design, including object inheritance: AlbumImage class inherits from Album class, almost entire program is built using interdependent functions
* Accessing a REST API or a new endpoint of a REST API that we have not included in any course (lecture or section) meeting or assignment: deep dream

#### Third level requirements:
* A piece of computational art as a result of writing code using data sources: deep dream collage of current top album covers

### Sources:
Lewis,Skyler(2017)lastfm-collage.txt(version 2)[GitHub gist] https://gist.github.com/alairock/6b0bc013023f240b8bcc67e278276a7f
