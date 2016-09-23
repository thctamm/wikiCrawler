# wikiCrawler
A simple wikipedia crawler that finds link-connections between articles.
Built with Flask, run on Heroku.

## Algorithm
The algorithm that the wiki crawler uses is not the most efficient one, nor does it find the shortest path, but rather it tries to mimick what a user would do.

The algorithm first finds all the links on the target website and saves them. Let's call these links degree 1 links. Then it goes into each of those links and finds and saves the links on those pages. Let's call these links degree 2 links.

Now the algorithm goes to the source page and checks if there's a link to the target page. If there is, then we're done. If not, then it finds all the degree 1 links and goes to a random one. If it didn't find one, then it looks for all the degree 2 links and goes to a random one. If it couldn't find a degree 2 link, then it goes to a random link on the page. Once the algorithm has gone to a new page, it tries to find direct, degreee 1 and degree 2 links again.

If a page has no links that have not been visited already, then the algorithm returns an empty path.

## Instructions

### Article connections
In order to find a connection from `source` to `target`, make the following http request:

```
GET wiki-crawler.herokuapp.com/wiki/source/target
```
And the response will be of the shape:

```
{
  "avg": 7.333333333333333, 
  "path": [
    "source", 
    "Article 1", 
    "Article 2", 
    "target"
  ]
}
```

Note: If nobody has ever search for a path to a `target` before, then the algorithm can take around 10 minutes to run, because it has to cache the degree 1 and degree 2 links.

### Number of views on Hillary Clinton's and Donald Trump's Wikipedia pages

make the following http request:

```
GET wiki-crawler.herokuapp.com/views
```
And the response will be of the shape, where the 0th element of each of the arrays is the number of page views on the corresponding US 2016 Presidential Election Candidate's wikipedia page 30 days ago, and the 29th element is the number of page views today.:

```
{
  "hillary": [
    4988, 
    6329, 
    4510, 
    2966, 
    2180, 
    4620, 
    4180, 
    5476, 
    5049, 
    4632, 
    3217, 
    1409, 
    3973, 
    5348, 
    5065, 
    6699, 
    4698, 
    3718, 
    5726, 
    10248, 
    7993, 
    7866, 
    6554, 
    6364, 
    3873, 
    3632, 
    5299, 
    5396, 
    4736, 
    4910, 
    3738
  ], 
  "trump": [
    5668, 
    6000, 
    5335, 
    3686, 
    3468, 
    5545, 
    4729, 
    7716, 
    7722, 
    6416, 
    3816, 
    2007, 
    4710, 
    6859, 
    6336, 
    7633, 
    5593, 
    4252, 
    5334, 
    8835, 
    7569, 
    8382, 
    7532, 
    7633, 
    4506, 
    3949, 
    7043, 
    7402, 
    6630, 
    6303, 
    4767
  ]
}
```
