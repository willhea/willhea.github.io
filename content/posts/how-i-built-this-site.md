---
title: "How I Built This Site"
date: 2025-09-03
summary: "Hugo static site generator with PaperMod theme."
tags: ["hugo", "static-site", "github-pages", "privacy", "goatcounter"]
---

In a [prior post](/posts/why-willhea/), I mentioned I wanted to create a personal site that was simple, low cost or free, easy to maintain, and relied on open source projects. This post details the build of this site that meets all of those goals.

*Note: I've migrated to Hugo from Pelican. This post is updated accordingly.*

## My Goals

My goals for the infrastructure for this site are:

1. Write content and posts in Markdown format
2. Create a static site from the Markdown files that loads quickly
3. Rely on a maintained, documented, open source backend
4. Use cheap/free hosting
5. Privacy friendly tracking & analytics
6. Simple customization

## Selecting a Build

For hosting, I chose **GitHub Pages** because it's free and one fewer service to setup and maintain.

For the static site generator, I chose **Hugo** with the **PaperMod** theme. Hugo is fast, well-documented, and has excellent theme support. PaperMod provides a clean, minimal design with dark mode support out of the box. *Note: I formerly used Pelican with a custom theme.*

## Building

This site works across two GitHub repos, one public and one private. The [public repo](https://github.com/willhea/willhea.github.io) holds the generated static site. The private repo holds the markdown files, Hugo config, and themes.

When a commit is pushed to the main branch of the private repo, it triggers a GitHub Action to build the site and push the outputs to the public repo.

## Styling

I adore simple black and white text and websites. It's one of the many reasons I keep coming back to [Notion](https://www.notion.com/). I block scripts and tracking on my browsers and convert any page I can into a simple reader. I also adore fast load times. I **hate** sites with auto-playing videos and other cruft.

PaperMod's default styling aligns well with these preferences. Clean, minimal, fast.

## Tracking & Metrics

I'm not writing this blog for pageviews. Still, it's useful to know who accesses this site, how often, and what they view. I don't need detailed information on every user.

I went with [GoatCounter](https://www.goatcounter.com/) because it's free for my use case and [dead simple to install](https://www.goatcounter.com/help/start) and maintain.

I like the setup so far and it's been extremely easy to update and maintain. It's inspired me to write, so it's already doing its job!
