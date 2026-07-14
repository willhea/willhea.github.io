---
title: "Dives"
description: "Interactive data Dives I built on MotherDuck — live, queryable visualizations of public datasets."
hideMeta: true
---

[MotherDuck Dives](https://motherduck.com/divemaxxing/) are interactive, AI-built data apps that query a live database in the browser. These are ones I made: each is a data pipeline I wrote plus a custom React view, reading real data on every load. Click through to explore them.

<div class="dive-cards">
  <article class="dive-card">
    <a href="https://motherduck.com/dive-gallery/dives/dive-into-claude-outages/" target="_blank" rel="noopener">
      <img src="/images/dives/claude-outages.webp" alt="Dive Into Claude Outages — charts and a world map of Anthropic status-page incidents">
    </a>
    <h3><a href="https://motherduck.com/dive-gallery/dives/dive-into-claude-outages/" target="_blank" rel="noopener">Dive Into Claude Outages</a></h3>
    <p>Every incident on Anthropic's public status page since March 2023, parsed into outage metrics and a timezone-aware world map. I built the Python pipeline that walks the Statuspage history feed and the React view that queries it live.</p>
  </article>

  <article class="dive-card">
    <a href="https://motherduck.com/dive-gallery/dives/nfl-coaching-tree/" target="_blank" rel="noopener">
      <img src="/images/dives/nfl-coaching-tree.webp" alt="NFL Coaching Tree — an interactive graph of who coached under whom">
    </a>
    <h3><a href="https://motherduck.com/dive-gallery/dives/nfl-coaching-tree/" target="_blank" rel="noopener">NFL Coaching Tree</a></h3>
    <p>Who trained under whom across every 2026 NFL head coach and coordinator, traced back through the head coaches they served under. An interactive graph you can walk branch by branch.</p>
  </article>
</div>
