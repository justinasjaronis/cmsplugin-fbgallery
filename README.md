cmsplugin-fbgallery
===================

Django CMS plugin for facebook album gallery

This projects helps integrate Facebook album into your Django CMS based website. The plugin provide superb performance compared to the Ajax based alternatives and works even on IE > 6 without any issues. Also, with caching enabled it loads fast without any lag.


## Installation:

```bash

```
And add the page id in your settings file:

```py
INSTALLED_APPS = (
                  `cmsplugin_gallery`,
                  )
                  
FB_PAGE_ID = '125976107506398'# Get the page Id from facebook album you want to use.

```


Once, done add a block into the django template where you want to use the plugin to work, preferably in
base.html:

```html

```

## Bugs/Issues

Create an issue here with proper detail: https://github.com/changer/cmsplugin-fbgallery/issues 


## Inspirations/Credits

This projects is inspired by the work of [@dantium](https://github.com/dantium) and [@driesdesmet](https://github.com/driesdesmet). 
