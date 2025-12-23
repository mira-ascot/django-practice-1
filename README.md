# Django Learning Summary

This project helped me understand Django’s core concepts by building a small “Monthly Tasks” app and improving it step by step while following Django conventions.

## Environment & Project Setup
- Used **Pipenv** to manage project-specific dependencies and virtual environments
- Learned how Django projects are created and structured
- Understood the role of core files (`settings.py`, `urls.py`, `manage.py`)
- Learned how apps are created, structured, and registered in `INSTALLED_APPS`

## Views & URL Routing
- Learned how Django views handle HTTP requests and return responses
- Mapped URLs to views using app-level and project-level `urls.py`
- Used dynamic URL segments with type converters (`<str>`, `<int>`)
- Replaced long conditional logic with dictionaries
- Handled invalid input using `HttpResponseNotFound`
- Used redirects and understood 3xx status codes
- Learned the importance of named URLs and `reverse()` for flexible routing

## Templates & Django Template Language (DTL)
- Rendered dynamic HTML using templates instead of raw strings
- Passed data from views to templates using context dictionaries
- Used template variables, filters, and tags (`for`, `if`, `url`)
- Learned why presentation logic belongs in templates, not views

## Template Inheritance & Reusability
- Avoided duplication by introducing a shared `base.html`
- Used template blocks for page-specific content
- Reused UI components using `{% include %}`

## Static Files
- Learned how Django expects static files to be structured
- Loaded CSS using `{% load static %}` and correct static paths
- Understood the difference between app-level and global static files
- Learned why static files stop working when `DEBUG = False`

## Error Handling
- Implemented a custom `404.html`
- Learned how Django automatically renders it when `Http404` is raised
- Understood the relationship between `DEBUG`, `ALLOWED_HOSTS`, and error pages

## Key Takeaways
- Django strongly enforces separation of concerns
- Named URLs and template inheritance improve maintainability
- Static file handling differs between development and production
- Building features incrementally helps Django’s conventions make sense
