# DiversityStyleGuide-GoogleDocs
Scrapes the Diversity Style Guide, references a google doc, and returns style guide entries that appear in the doc

<<<<<<< HEAD
## About the code
I created this to encourage more newsrooms to adopt the Diversity Style Guide and to make it easier for writers and editors to ensure they're following the Diversity Style Guide guidelines. However, this isn't a replacement for checking the [Diversity Style Guide website](https://www.diversitystyleguide.com/), especially for sensitive stories.

## Getting started
Before you use the code, you'll need to set up a google app scrips api.

First, go to the [Google Cloud Platform](https://console.cloud.google.com/). Create a new project, and go into the API settings. Create an OAuth 2.0 client id for desktop. Download the json access file. You will need the filepath later.

There are two ways to add the filepath. First, you can use the `GoogleDocReferenceDivStyleGuide().API_KEY_init()` method. Or, you can skip to the run method. If the API key is missing, it will ask for it and save the variable locally.
=======
## Getting started
Before you use the code, you'll need to set up a google app scrips api.

First, go to the [Google Cloud Platform](https://console.cloud.google.com/). Create a new project, and go into the API settings. Create an OAuth 2.0 client id for desktop. Download the json access file.

Now, in the code, you'll have to make one change in order to access your API. In the `__init__` method, replace `YOUR API KEY FILENAME HERE` with the filepath for the file you just downloaded

## How to use
There are two ways to run this script: either scrape the Diversity Style Guide and reference with a Google Doc all at once, or save the scraped style guide as a variable, so you can reference multiple docs in a row.

### Scrape and Reference a doc all at once
If you want to scrape the style guide and reference a doc all at once, use the following code. This is easiest when you only have one doc to read.

```python
url = GoogleDocReferenceDivStyleGuide(#url to google doc here)
url.ScrapeAndReference()
```
>>>>>>> 22304cb4bc450cdcff1e1966fef1f2b9326bc29c

## How to use
In order to run the script, import DiversityStyleGuide as a module and then use the run function:
```
from DiversityStyleGuide import GoogleDocReferenceDivStyleGuide

GoogleDocReferenceDivStyleGuide().run()
```

<<<<<<< HEAD
The first time you run the function, it will scrape the Diversity Style Guide from its website and save locally (using pickle). Every other time, it will ask you if you want to rescrape or use the version saved locally.
=======
### Just scrape and individually reference
This is useful for when you have multiple docs to reference and don't want to rescrape the style guide each time
>>>>>>> 22304cb4bc450cdcff1e1966fef1f2b9326bc29c

When it runs the Google oauth, it will ask you if you want to save the oauth for future use, so you don't have to reauthenticate every time you run the program. If you choose not to save, next time you run the program, you'll have to reauthenticate. If you save authentication, each future use will ask you if you want to use the saved oauth authentication or reauthenticate.

The run method can scrape and reference up to five Google Docs. The more you scrape at one time, the more scrolling you'll have to do once the program finishes running. It will ask you how many you want to scrape. For each, it will then ask you for the url of the Doc. It will iterate through each Doc, reading the text and referencing with the scraped Diversity Style Guide