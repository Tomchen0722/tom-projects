from pathlib import Path

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import (
    UnicodeCIDFont
)

pdfmetrics.registerFont(
    UnicodeCIDFont(
        "MSung-Light"
    )
)

styles = getSampleStyleSheet()


class PDFExporter:

    def export(
            self,
            output_file,
            meeting_title,
            summary,
            transcript,
            actions=None,
            decisions=None):

        doc = SimpleDocTemplate(
            output_file
        )

        story = []

        title_style = styles["Title"]
        body_style = styles["BodyText"]

        story.append(
            Paragraph(
                f"<b>{meeting_title}</b>",
                title_style
            )
        )

        story.append(
            Spacer(1, 20)
        )

        story.append(
            Paragraph(
                "<b>會議摘要</b>",
                body_style
            )
        )

        story.append(
            Paragraph(
                summary.replace(
                    "\n",
                    "<br/>"
                ),
                body_style
            )
        )

        story.append(
            Spacer(1, 10)
        )

        if decisions:

            story.append(
                Paragraph(
                    "<b>決策事項</b>",
                    body_style
                )
            )

            for item in decisions:

                story.append(
                    Paragraph(
                        f"• {item['decision']}",
                        body_style
                    )
                )

        if actions:

            story.append(
                Paragraph(
                    "<b>待辦事項</b>",
                    body_style
                )
            )

            for item in actions:

                story.append(
                    Paragraph(
                        f"• {item['owner']}："
                        f"{item['task']}",
                        body_style
                    )
                )

        story.append(
            PageBreak()
        )

        story.append(
            Paragraph(
                "<b>逐字稿</b>",
                body_style
            )
        )

        story.append(
            Paragraph(
                transcript.replace(
                    "\n",
                    "<br/>"
                ),
                body_style
            )
        )

        Path(output_file).parent.mkdir(
            exist_ok=True
        )

        doc.build(
            story
        )

        return output_file


_exporter = PDFExporter()


def export_pdf(
        output_file,
        meeting_title,
        summary,
        transcript,
        actions=None,
        decisions=None):

    return _exporter.export(
        output_file,
        meeting_title,
        summary,
        transcript,
        actions,
        decisions
    )