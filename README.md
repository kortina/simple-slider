# Simple Slider

Great (and powerful) tools for creating slideshows from markdown exist: [gnab/remark](https://github.com/gnab/remark), [reveal.js](https://github.com/hakimel/reveal.js/).

But the markdown still feels a *little* heavy sometimes.  Using `---` for slide breaks is particularly annoying.

This is a very simple slider that makes stupid assumptions about (1) what elements will render on a new slide and (2) what constitutes speaker notes.

See the [example slide](https://gist.githubusercontent.com/kortina/66d1263fe538b30f4a489d8c97faa140/raw/4fff2f6f196689e3519f9f2945c016e1b79f8fd3/very-simple-slide-example.md) for full details.

#### Summary

- h1, h2, h3 - render a new slide
- img - renders a new slide
- horizontal rule (`---`) - forces a slide break
- h4, h5, h6 - render as part of the current slide (in case you want multiple lines of text)

Want an iframe embed? Put it in an h1:

```markdown
# <iframe width="560" height="315" src="https://www.youtube.com/embed/UcU04NGMQb8" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

Hit `n` to show speaker notes. Hit `?` to show more keyboard shortcuts.

That's about it.

#### Development

```sh
./serve_dev.py # python3 script to serve index.html
```