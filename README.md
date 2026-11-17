# HSMA Content Writing Manual

A guide to writing content for HSMA sessions, built as a [Quarto](https://quarto.org/) book.

## Requirements

- [Quarto](https://quarto.org/docs/get-started/) (tested with 1.11)
- Python 3 (only used to zip the rendered book)

The `bergam0t/value-box` extension is already included in `_extensions/`, so you don't need to install anything else.

## Previewing while you write

```bash
quarto preview
```

This opens the book in your browser and reloads it when you save a chapter.

## Building the book (website + zip)

```bash
quarto render
```

This builds the full book as a website in `_book/`. Each chapter is a separate page, with the sidebar for moving between them.

When the render finishes, `scripts/zip_book.py` zips the whole of `_book/` into:

```
_book/HSMA-Content-Writing-Manual.zip
```

Use the zip when someone needs the manual offline. They unzip it and open `index.html` inside the `HSMA-Content-Writing-Manual` folder. The navigation and links work, but the search box may not, because browsers usually block it when pages are opened from local files.

The zip is only made by a full `quarto render`, not by `quarto preview` or by rendering a single chapter.

## Building the single-file version

```bash
quarto render --profile standalone
```

This builds the whole manual as **one self-contained HTML file**:

```
_standalone/HSMA-Content-Writing-Manual.html
```

Fonts, images, styling and scripts are all embedded in the file, so you can email it or put it on a shared drive and it opens anywhere, with no other files needed. It has a table of contents on the left instead of the book's sidebar. Quarto also copies `assets/` and `resources/` into `_standalone/`, but the HTML doesn't use them; share just the `.html` file.

How it works:

- `HSMA-Content-Writing-Manual.qmd` pulls in each chapter with `{{< include >}}`.
- `_quarto-standalone.yml` is a [Quarto profile](https://quarto.org/docs/projects/profiles.html) that builds only that file, into `_standalone/`, with `embed-resources: true`. It uses the same theme, fonts and filters as the book.
- `scripts/standalone_links.lua` rewrites links between chapters (e.g. `[see here](hsma_tech_stack.qmd)`) so they jump to that chapter within the page.

## Adding or reordering chapters

The chapter list is in **two** places, and both need updating:

1. `book: chapters:` in `_quarto.yml`. This controls the book.
2. `HSMA-Content-Writing-Manual.qmd`. This controls the single-file version. Each chapter is wrapped in a div whose id is `chapter-` followed by the filename without `.qmd`:

   ```markdown
   ::: {#chapter-my_new_chapter}
   {{< include my_new_chapter.qmd >}}
   :::
   ```

   The single-file links between chapters rely on that id.

Every chapter should start with a level-one heading (`# Chapter Title`). Without one, its sections end up under the previous chapter in the single-file version.

To link to another chapter, link to its `.qmd` file, e.g. `[pacing](pacing_and_prior_knowledge.qmd)`. This works in both the book and the single-file version.

## Don't add `embed-resources` to the book

Don't set `embed-resources: true` in `_quarto.yml`. In a multi-page book, Quarto embeds the neighbouring chapter pages into each page as well, so every page balloons to tens of megabytes, and it still doesn't give you one file. Use the standalone profile instead.
