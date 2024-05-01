from langchain.tools import StructuredTool
from pydantic.v1 import BaseModel

def write_report(filename, html):
    try: 
        with open(filename, 'w') as f:
            f.write(html)
        return f"Report successfully saved to {filename}."
    except Exception as e:
        return f"Failed to write report: {str(e)}"

class WriteReportArgsSchema(BaseModel):
    filename: str
    html: str

# Need to use StructuredTool because it receives multiple arguments
write_report_tool = StructuredTool.from_function(
    name="write_report",
    description="Write an HTML file to disk. Use this tool whenever someone asks for a report.",
    func=write_report,
    args_schema=WriteReportArgsSchema
)