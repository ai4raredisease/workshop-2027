# JSPS–DFG–GA4GH Workshop 2027

Bilingual static website for the Japan–Germany workshop on 20–23 February 2027 at Keio University CRIK, Tokyo. Japanese is the default language; English is under `/en/`. Built with semantic HTML and responsive CSS; no JavaScript, dependencies, or build step.

## Preview locally

From this directory, run:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open http://127.0.0.1:8000/ for Japanese or http://127.0.0.1:8000/en/ for English. Stop the server with Ctrl+C. Refresh after saving edits.

## Directory structure

```text
index.html              Japanese workshop text and program entries
en/index.html           English workshop text and program entries
assets/css/styles.css   Typography, colors, layout, mobile and print styles
assets/images/          Reserved for future images (currently empty)
.nojekyll               Bypasses Jekyll processing on GitHub Pages
.gitignore              Excludes local IDE and operating-system files
README.md               Editing and publishing instructions
```

The empty images directory is not tracked by Git until an image is added. Use relative asset paths such as `assets/images/venue.jpg` so the site also works under a GitHub Pages repository URL.

## Edit speakers

In both `index.html` and `en/index.html`, find the `SPEAKERS` comment and the `speaker-grid` container. Each participant has an article with the `speaker-card` class. The first two articles are in `keynote-grid` and also have `keynote-card`; they include a keynote label and talk title. `data-status="confirmed"` records the three explicitly confirmed Japanese speakers without displaying a status next to their names. Edit the name in its `<h3>`, affiliations in the first paragraph, and country in the `country` paragraph. Copy an entire article to add a person. Do not add titles or confirmation claims without checking them.

Cards can later accommodate portraits by adding an image before the name and corresponding CSS. Provide appropriate alternative text and explicit image dimensions. No photos are currently required.

## Edit the program

Update both language pages together. Find the `PROGRAM` comment. Each day is a `program-day` section containing an ordered `sessions` list. Each `<li>` includes a `session-time` span, a talk title in `<h4>`, and an optional speaker paragraph. Copy a list item to add a session. Keep the `interval` class for lunch and breaks; omit speaker paragraphs when speakers are unspecified.

Keep day IDs unique (`day-0`, `day-1`, `day-2`, `day-3`) so the day navigation works. Times are local to Tokyo (JST). Keep the preliminary status until the program is finalized.

## Add the future Google Form registration URL

Each language page has two disabled registration buttons: one in the hero and one in the Registration section. Once the real public form URL is available, replace **all four** buttons with links, for example:

```html
<a class="button" href="PASTE_ACTUAL_GOOGLE_FORM_URL_HERE">Register for the Workshop</a>
```

Replace the placeholder with the actual URL before publishing. Update the registration status text in both languages. Do not retain a `disabled` attribute on links. Links open in the same tab by default. No embedded form or JavaScript is needed.

## Other content updates

HTML comments mark the main editable areas. The Venue section identifies Keio University CRIK and links to its official website. Add address, access details, and map links only when supplied and confirmed. Add travel information there if useful. Keep date references, metadata, event overview cards, and the detailed program aligned in both languages. Replace the Contact placeholder with verified details. Use `&amp;` for ampersands in HTML text.

## Publish with GitHub Pages

When ready, commit the website files and push them to the repository's `main` branch. In the repository on GitHub:

1. Open **Settings → Pages**.
2. Under **Build and deployment**, choose **Deploy from a branch**.
3. Select **main** and **/(root)**, then save.
4. Wait for deployment to complete and open the site URL shown in Pages settings.

Subsequent pushes to that branch update the published site. No custom Actions workflow is needed for this structure. This setup has not yet been enabled by this implementation.

Before publishing, preview on desktop and mobile, check the navigation with a keyboard, verify confirmed details, and test any external links you add.

## Current program and editorial notes

- Day 0: Saturday, 20 February 2027, pre-conference hands-on seminar, 13:00–17:30. The nine-entry timetable follows the subsequently supplied explicit start/end times. The separate 90/60/90-minute summary differs from those times and is not displayed; confirm that summary before using it to revise the schedule.
- Day 1: Sunday, 21 February 2027, main scientific workshop. The 14 program entries follow the latest supplied English titles and times, with Japanese translations. Keynotes are Kenjiro Kosaki and Peter N. Robinson.
- Day 2: Monday, 22 February 2027, collaborative hackathon. Detailed schedule pending.
- Day 3: Tuesday, 23 February 2027 (Japanese public holiday), consortium wrap-up and networking / excursion. Detailed schedule pending.
- The unscheduled gaps at 11:00–11:05 and 15:50–16:00 are retained. No speaker is assigned to the 16:00–17:00 practical session. Lunch-box provision is tentative.
- Soichi Ogishima is listed only in the preliminary program. Koh-ichiro Yoshiura remains in the participant section from the original page because his participation was not explicitly withdrawn.
- Both pages use the same stylesheet. Japanese links to `en/`; English links back through `../`, keeping navigation compatible with GitHub Pages repository subpaths.
