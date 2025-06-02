import lxml.etree
from xmldiff import formatting
from os import path

xslt_path = path.join(path.dirname(__file__), "html_formatter.xslt")
XSLT = open(xslt_path, "r").read()
XSLT_TEMPLATE = lxml.etree.fromstring(XSLT, parser=None)


class HTMLFormatter(formatting.XMLFormatter):
    def render(self, result):
        transform = lxml.etree.XSLT(XSLT_TEMPLATE)
        result = transform(result)
        return super(HTMLFormatter, self).render(result)
