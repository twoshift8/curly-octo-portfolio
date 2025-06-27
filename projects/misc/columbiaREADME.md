#Columbia Job Helper

Tampermonkey Script Built with ChatGPT's Help

This script helps streamline job searching on Columbia University's job board targeted specifically for research positions.

### What It Does
    Auto-selects “Research” filter on Columbia’s job page (since the site annoyingly forgets your filters)

    Asks how many listings you want to open

    Automatically opens the top N results in new tabs (bypassing Columbia’s broken ctrl+click behavior)

---
### Why I Made It
Searching Columbia’s job board was tedious, since filters saved inconsistently, and opening multiple listings meant constant backtracking and re-clicking and scrolling to double check if the cookie decided to save or not, and a constant headache just to encounter jobs I'm not interested in.

I couldn't get Python to integrate with a browser, nor streamline functionalities in extensions for persistence between sessions/profiles/devices/etc. I tried a few approaches, but it was just too messy. This means I needed a favor from the intimidating Godfather of programming: JavaScript. 

I haven't yet learned JS, but I leveraged my Python background and worked with ChatGPT to figure out how to automate the process using Tampermonkey, and this has saved me hours. 

---
### How to Use

    1- Install Tampermonkey in your browser.

    2 - Add this script.

    3 - Go to Columbia’s Job Search Page.

    4 - Click the Tampermonkey menu > “▶ Open Top N Columbia Listings.”

    5 - Input how many job listings you want to open, starting from the top.

    6 - Each job listing will open in a new tab.

---
### What It Shows
By *no* means am I a JS expert, and that's not what this is meant to demonstrate. To me, this codifies my flexibility to overcome real obstaches and resolve problems using every tool at my disposal. I used ChatGPT to build this script, combining my programming logic from Python with AI assistance. Now, I have a working tool that does exactly what I needed, and I know how to implement more in the future.

---
### What It Doesn't Do

    It doesn’t apply for jobs (more details available upon inquiry).

    It doesn’t store or track anything, just runs locally in your browser like any extension.

--- 
### A Note on AI Involvement
Again, I don’t (yet) speak JavaScript. I provided the logic and iterative guidance, and was a ChatGPT coding assistant which helped implement it in JavaScript. I hope this shows that I know how to identify issues, break down problems logically, and effectively leverage and work in cooperation with AI to overcome challenges I'm not (yet) fully equipped for on my own.