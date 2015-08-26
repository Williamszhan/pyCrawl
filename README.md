# How to make a perfect crawl

## Incremental Crawler

Keep crawling the web and refresh regularly.

## High performance

Using effcient data structure to build a better crawler.

## Distributed crawlers

Make your crawler extensible.

2 types: `Master-Slave` / `Peer to Peer`

## Robust

Make sure your crawler can recover working when suffer error last time.

## Friendly

There are two points: 

obey the website's protocols(robot.txt) or the mark in HTML

Don't crawl the same website frequently.

such like:

```HTML

Disallow: /tmp/

<meta name="robots" content="noindex">
<meta name="robots" content="nofollow">

```

# How to assess the quality of crawler

1. Coverage

2. Importance

3. Recently
