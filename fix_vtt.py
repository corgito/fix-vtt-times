"""
fix_vtt.py: A Python script to adjust the timings in VTT caption files.
My spin on Nat Dunn's WebVTT timestamp adjustment script. See https://www.webucator.com/article/fixing-webvtt-times-with-python/
This version changes Nat's in two ways:
1. I use the pyperclip module to skip a step and copy the contents of the output to the clipboard.
To install pyperclip see: https://github.com/asweigart/pyperclip
2. The output of the fix_vtt_times function on its own produces three trailing zeros. YouTube doesn't like this. So output in my version is formatted to remove the last three leading zeros.
By Nicolai Haddal: nhaddal [at] protonmail.com
"""


from datetime import datetime, timedelta
import pyperclip


def fix_vtt_times(vtt_input, seconds):
    """Fixes times in WebVTT by adding the passed-in seconds to all the timestamps.

    Args:
        vtt_input (str): The text of the WebVTT
        seconds (float): The seconds to add. Use negative number to subtract.
    """
    td = timedelta(seconds=seconds)
    dt_format = "%H:%M:%S.%f"
    vtt_output = ""

    for line in vtt_input.splitlines():

        if "-->" not in line:
            # This line doesn't have times. Just append it as is.
            vtt_output += line + "\n"
            continue

        start, end = line.split(" --> ")
        start = start.strip()
        end = end.strip()

        start_time_fixed = datetime.strptime(start, dt_format) + td
        end_time_fixed = datetime.strptime(end, dt_format) + td

        start_time = start_time_fixed.strftime(dt_format)
        end_time = end_time_fixed.strftime(dt_format)

        vtt_output += f"{start_time[:-3]} --> {end_time[:-3]}\n"

    return vtt_output


# Insert the contents of your VTT file in the triple quotes below:
vtt = """COPY VTT CONTENTS HERE"""

# Replace zero below with the number of seconds you need to adjust.
# Say you cut five minutes from the beginning. Replace 0 with -300

pyperclip.copy(fix_vtt_times(vtt, 0))
