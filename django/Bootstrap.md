# Using Bootstrap in Django

## New folder static

```python
-blog
-templates
-static
　└bootstrap
　　└css
  　└js
　└jquery
　└popper
```

> settings.py

```python
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    [
        os.path.join(BASE_DIR, "static"),
    ]
)
```

> html

```python
{ % load static % }
<html>
  <head>
    <link rel="stylesheet" href="{% static  'bootstrap/css/bootstrap.min.css' %}">
    <script type="text/javascript" src="{% static 'jquery/jquery-3.4.1.js' %}"></script>
    <script type="text/javascript" src="{% static 'bootstrap/js\bootstrap.min.js' %}"></script>
  </head>
  <body>
  </body>
</html>
```

