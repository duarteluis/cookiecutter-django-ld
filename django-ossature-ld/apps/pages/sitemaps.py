from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    # protocol = 'https'

    def items(self):
        return [
            "home",
            "faq",
            "privacy",
            "terms",
        ]

    def location(self, item):
        return reverse(item)
