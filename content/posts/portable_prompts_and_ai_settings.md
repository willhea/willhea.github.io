---
title: "Portable Prompts and AI Settings"
date: 2026-05-06
summary: "Use a git repo to sync skills and preferences across devices and tools."
tags: ["ai", "prompts"]
---
I like to switch computers and operating systems, but I want my AI prompts, skills, and preferences to follow me from computer to computer. The way I do that is by: 
1. Storing prompts and skills in a "Prompts" folder. That folder is in the same location on each of my computers (e.g., ~/path/to/prompts). 
2. Using git to track, commit, and pull changes with a private GitHub repo as my remote repository. 
3. Symlinking that folder into each AI agent's expected skills directory. For example: ln -s ~/path/to/prompts/skills ~/.claude/skills

That single symlink covers Claude Code (which reads ~/.claude/skills/ natively) and OpenCode (which reads it as a fallback). Other agents like Pi get their own symlink to the same source folder.

I similarly use a dotfiles folder and repo for configuration files for my applications. 

This setup means the prompts repo is agent-agnostic, the per-agent step is just a symlink, and I can swap between harnesses while keeping my skills available. 
