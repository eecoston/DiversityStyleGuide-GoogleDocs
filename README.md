# DiversityStyleGuide-GoogleDocs
Scrapes the [Diversity Style Guide](https://www.diversitystyleguide.com/), references a google doc, and returns style guide entries that appear in the doc

## About the code
I created this code to encourage more newsrooms to adopt the [Diversity Style Guide](https://www.diversitystyleguide.com/), and to provide a quick way for reporters and editors to do a general check of their article draft. Note: this program is not perfect and does not replace checking the style guide website, especially for sensitive stories.

## Getting started
Before you use the code, you'll need to set up a google app scrips api.

First, go to the [Google Cloud Platform](https://console.cloud.google.com/). Create a new project, and go into the API settings. Create an OAuth 2.0 client id for desktop. Download the json access file. You will need the filepath later.

There are two ways to add the filepath. First, you can use the `GoogleDocReferenceDivStyleGuide().API_KEY_init()` method. Or, you can skip to the run method. If the API key is missing, it will ask for it and save the variable locally.

## How to use
Import the style guide and use the run method to use the function. 
```python
from DiversityStyleGuide import GoogleDocReferenceDivStyleGuide

GoogleDocReferenceDivStyleGuide().run()
```

or run the file in the shell:
```python
python DiversityStyleGuide.py
```

The first time you run the function, it will scrape the [Diversity Style Guide](https://www.diversitystyleguide.com/) from its website and save locally (using pickle). Every other time, it will ask you if you want to rescrape or use the version saved locally, which saves a lot of time.

You also have the option to save your oauth authentication locally, allowing you to avoid reauthenticating every single time you use the run method. If you save authentication, it will ask you if you want to reauthenticate or used the saved version.

The run method has the functionality to scrape and reference up to 5 Google Doc files. It will ask how many you want to scrape, and then ask for the url for each. The more docs you scrape at once, the more scrolling you'll have to do once the program finishes.

For every style guide word found in the doc, the run method will return the location of the word in the doc, and the term and usage guidance from the style guide.
