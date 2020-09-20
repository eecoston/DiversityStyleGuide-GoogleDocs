# DiversityStyleGuide-GoogleDocs
Scrapes the Diversity Style Guide, references a google doc, and returns style guide entries that appear in the doc

## Getting started
Before you use the code, you'll need to set up a google app scrips api.

First, go to the [Google Cloud Platform](https://console.cloud.google.com/). Create a new project, and go into the API settings. Create an OAuth 2.0 client id for desktop. Download the json access file.

Now, in the code, you'll have to make one change in order to access your API.

On line 35, change the `YOUR API FILE PATH HERE` to the filepath for the file you just downloaded. 

## How to use
There are two ways to run this script: either scrape the Diversity Style Guide and reference with a Google Doc all at once, or save the scraped style guide as a variable, so you can reference multiple docs in a row.

### Scrape and Reference a doc all at once
If you want to scrape the style guide and reference a doc all at once, use the following code. This is easiest when you only have one doc to read.

```python
url = GoogleDocReferenceDivStyleGuide(#url to google doc here)
url.ScrapeAndReference()
```

It will return the the character number of the word where it appears in the doc, the term, and guidance from the style guide on how to use the term.


### Just scrape and individually reference
This is useful for when you have multiple docs to reference and don't want to rescrape the style guide each time

To scrape the style guide:
```python
DiversityStyleGuide = GoogleDocReferenceDivStyleGuide('').StyleGuideScraper()
```
If you print the `DiversityStyleGuide` variable, it will show a python dictionary of the style guide.

To reference a doc:
```python
url = GoogleDocReferenceDivStyleGuide(#url to google doc here)
url.justReference(DiversityStyleGuide)
```
