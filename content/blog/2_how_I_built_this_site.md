---
Title: How I Built This Site
Date: 2025-09-03
Status: published
Category: blog
Tags: 
Slug: how_i_built_this_site
Summary: Pelican Python static site generator.
--- 
In a [prior post]({filename}/blog/1_why_willhea.md), I mentioned I wanted to create a personal site that was simple, low cost or free, easy to maintain, and relied on open source projects with a preference for Python. This post details the build of this site that meets all of those goals.

# My Goals
My goals for the infrastructure for this site are: 
1. Write content and posts in Markdown format
2. Create a static site from the Markdown files that loads quickly
3. Rely on a maintained, documented, open source backend with a preference for Python
4. Use cheap/free hosting
5. Privacy friendly tracking & analytics
6. Customize the site in Python

# Selecting a Build
It feels like cheating, but to find a solution, I prompted [Perplexity](https://www.perplexity.ai/). It recommended: 

Hosting: 
- [GitHub Pages](https://docs.github.com/en/pages/quickstart)
- [Hostinger](https://www.hostinger.com/1)
- [Netlify](https://www.netlify.com/)
- [Vercel](https://vercel.com/)

**GitHub Pages** immediately stood out to me by being free and one fewer service I need to setup and maintain. 

Static Site Generator: 
- [MkDocs](https://www.mkdocs.org/)
- [Nikola](https://getnikola.com/)
- [Pelican](https://docs.getpelican.com/en/latest/)

I perused documentation and site examples and narrowed it down to Nikola and Pelican. Both looked excellent (I may end up trying both in the future), but I went with **Pelican** because I liked the [GitHub Pages documentation](https://docs.getpelican.com/en/latest/tips.html) and the example sites looked more than good enough for my needs. 

# Building
I love [Replit](https://replit.com/), but I want to build this site in a local environment to work on my coding skills and make it easier to maintain and work on offline. I travel often and frequently don't have strong wifi. I want to be able to write and work on the site at any time with or without an internet connection.

For deployment, this site works across two GitHub repos, one public and one private. The [public repo](https://github.com/willhea/willhea.github.io) holds the code for this site. The private repo holds the markdown files, Pelican, and other backend code.

When a commit is pushed to the main branch of the private repo, it triggers a GitHub Action to run the code and push the outputs of the static site generator into the public repo. The [Pelican documentation](https://docs.getpelican.com/en/latest/tips.html) provides more detail. 

# Styling
I adore simple black and white text and websites. It's one of the many reasons I keep coming back to [Notion](https://www.notion.com/). I block scripts and tracking on my browsers and convert any page I can into a simple reader. I also adore fast load times. I **hate** sites with auto-playing videos and other cruft.

I used the default simple theme and made some CSS modifications with the help of AI. The current styling is similar to what I built on my homebrew Replit site. The look and feel is heavily inspired by [Matt Leaverton's personal site](https://www.mattleaverton.com/) that also runs on Pelican. Matt, we've never met, but I like your style. 

# Tracking & Metrics
I'm not writing this blog for pageviews. Still, it's useful to know who accesses this site, how often, and what they view. I don't need detailed information on every user. The three primary options I considered were: 
1. [GoatCounter](https://www.goatcounter.com/)
2. [Plausible Analytics](https://plausible.io/)
3. [Google Analytics](https://marketingplatform.google.com/info?authuser=0) (free version)

Google Analytics is interesting because it would be a great opportunity to play with a tool I would use elsewhere. At the same time, I favor privacy, I think Google's tracking is excessive and invasive, and I block those trackers as a user in my own browsing. If it would annoy me, I'm not going to do it to my users. 

I went with GoatCounter because it's free for my use case and [dead simple to install](https://www.goatcounter.com/help/start) and maintain. 

I like the setup so far and it's been extremely easy to update and maintain. It's inspired me to write, so it's already doing its job!