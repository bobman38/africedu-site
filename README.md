# Africedu website

Please use `virtualenv` to install properly python dependencies !

This website is powered by the [Pelican](http://docs.getpelican.com/en/3.6.3/index.html) framework.

## Install deps

```
workon pelican
pip install pelican markdown beautifulsoup4 ghp-import
```

## Run the site locally

```
make serve
```

## Push on github pages

```
make github
```
