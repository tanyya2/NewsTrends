## README file

# TechTrends

TechTrends is an application that fetches the newest tech trends from a few different sources. A user creates a profile with a list of interests. After that, the user is able to pick an article of interest and request a summary. Articles are tracked in the database to avoid showing the same article multiple times.

## Who is it for

Developers, students, and anyone interested in tech who wants a quick way to catch up on tech news without searching through multiple websites and full length articles.

## How the Data Is Stored

A local SQLite database holds two main tables:

- users: user_id, username, interests, created_at
- articles: article_id, title, url, source, publication_date, and a read status used to avoid repeating articles

## Tech Stack

- SQLite
- Hacker News API
- Google Gemini API
- NY Times API
- BeautifulSoup API
- Flask
- React
