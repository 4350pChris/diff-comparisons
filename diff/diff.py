from utils.utils import get_proper_path
from difflib import HtmlDiff
from xmldiff import main as xml, formatting
import lxml.etree


def read_file_and_split(file: str) -> list[str]:
    """
    Reads a file and splits it into lines.
    """
    with open(get_proper_path(file), 'r', encoding='utf-8') as f:
        return f.read().splitlines()


def text_diff(left: str, right: str):
    left_lines = read_file_and_split(left)
    right_lines = read_file_and_split(right)

    return HtmlDiff(wrapcolumn=60).make_file(
        left_lines,
        right_lines,
        context=True,
        numlines=1,
    )


XSLT = u'''<?xml version="1.0"?>
 <xsl:stylesheet version="1.0"
    xmlns:diff="http://namespaces.shoobx.com/diff"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template match="@diff:insert-formatting">
        <xsl:attribute name="class">
          <xsl:value-of select="'insert-formatting'"/>
        </xsl:attribute>
    </xsl:template>

    <xsl:template match="diff:delete">
        <del><xsl:apply-templates /></del>
    </xsl:template>

    <xsl:template match="diff:insert">
        <ins><xsl:apply-templates /></ins>
    </xsl:template>

    <xsl:template match="*[ @diff:delete ]">
        <xsl:copy>
            <xsl:apply-templates select="@*[namespace-uri() != 'http://namespaces.shoobx.com/diff']"/>
            <del>
                <xsl:apply-templates select="node()" />
            </del>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="@* | node()">
      <xsl:copy>
        <xsl:apply-templates select="@* | node()"/>
      </xsl:copy>
    </xsl:template>
 </xsl:stylesheet>'''

XSLT_TEMPLATE = lxml.etree.fromstring(XSLT)


class HtmlFormatter(formatting.XMLFormatter):
    def render(self, result):
        """
        Render the XML diff result as HTML.
        """
        transform = lxml.etree.XSLT(XSLT_TEMPLATE)
        result = transform(result)
        return super(HtmlFormatter, self).render(result)


def xml_diff(left: str, right: str):
    formatter = HtmlFormatter(
        text_tags=('LA')
    )
    return xml.diff_files(
        get_proper_path(left),
        get_proper_path(right),
        formatter=formatter,
        diff_options={'fast_match': True, 'ratio_mode': 'accurate', 'F': 0.5}
    ).__str__()
