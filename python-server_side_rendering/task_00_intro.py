"""
Python module to use Server-Side Rendering
"""
import os


def generate_invitations(template, attendees):
    """
    Function to create a Simple Templating Program
    """
    if not template or template == "":
        return ("Template is empty, no output files generated")
    
    if not isinstance(template, str):
        return ("template must be a string")
    
    if not attendees:
        return ("No data provided, no output files generated.")
    
    if not isinstance(attendees, list):
        return ("attendees must be a list")
    
    for _dict in attendees:
        if not isinstance(_dict, dict):
            return ("each element in attendees must be a dictionary")
    """
    """
    try:
        for id, _dict in enumerate(attendees):
            if _dict["name"] is None:
                _dict["name"] = "name: N/A"
            replace_str = template.replace("{name}", _dict["name"])
            if _dict["event_title"] is None:
                _dict["event_title"] = "event_title: N/A"
            replace_str = replace_str.replace(
                "{event_title}", _dict["event_title"])
            if _dict["event_date"] is None:
                _dict["event_date"] = "event_date: N/A"
            replace_str = replace_str.replace(
                "{event_date}", _dict["event_date"])
            if _dict["event_location"] is None:
                _dict["event_location"] = "event_location: N/A"
            replace_str = replace_str.replace(
                "{event_location}", _dict["event_location"])

            output_file_name = f"output_{id + 1}.txt"
            if os.path.exists(output_file_name):
                pass
            else:
                with open(output_file_name, "w", encoding="utf-8") as txt_file:
                    txt_file.write(replace_str)

    except Exception as e:
        return (f"Error occured: {str(e)}")
