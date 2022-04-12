"""
This module generates HTML string based on the calendar data.
"""
__author__ = 'Suparna S. Nair'


def generator_head():
    """
    This function generates the head of the html file, including  the styling.
    :return: the generated html string
    """
    html_data = \
    """
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Calendar Generator</title>
         
    """
    # the css styling for the file
    html_data += \
    """
    <style>
        body {
            font-family: 'verdana';
        }
        .grid-container {
          display: grid;
          grid-template-columns: auto auto auto;
          // background-color: #2196F3;
          padding: 5px;
        }
        .grid-item {
          // background-color: rgba(255, 255, 255, 0.8);
          padding: 5px;
          font-size: 10px;
          text-align: center;
        }
        table {
            border: 1px solid rgba(0, 0, 0, 0.8);
            border-collapse: collapse;
            background: white;
            color: black;
        }
        h1 {
            text-align:center;
        }
        th,
        td {
            // font-weight: bold;
        }
    </style>
    </head>
    <body>
        """
    return html_data


def generate_tail():
    """
    This function generates the tail end of the html file
    :return: the generated html string
    """
    html_data = """
    </body>
    </html>
    """
    return html_data


def generate_body(data):
    """
    This function generates the body of the html output
    :param data: the data in form of dict containing calendar info
    :return: the generated html string
    """
    html_data = ""
    # generate a grid container for each year in the dict
    for year in data:
        html_data += "<h1>Calendar of " + str(year) + "</h1>" + \
        """
        <div class="grid-container">
        """
        # now, generate calendar for all 12 months in the given year
        for month in data[year]:
            html_data += \
            """
              <div class="grid-item">
                <h2 align="center" style="color: orange;">""" + str(month) + " " + str(year) + \
            """
                </h2>
                <br />
                <table bgcolor="lightgrey" align="center"
                    cellspacing="21" cellpadding="21">
                    <caption align="top">
                    </caption>
                    <thead>
                        <tr>
                            <th style="color: white; background: purple;">
                                Mon</th>
                            <th style="color: white; background: purple;">
                                Tue</th>
                            <th style="color: white; background: purple;">
                                Wed</th>
                            <th style="color: white; background: purple;">
                                Thu</th>
                            <th style="color: white; background: purple;">
                                Fri</th>
                            <th style="color: white; background: #620070;">
                                Sat</th>
                            <th style="color: white; background: #620070;">
                                Sun</th>
                        </tr>
                    </thead>
                """
            html_data += \
                """
                <tbody>
                    <tr>
                """
            # remove the complete row if all days are empty spaces
            if all(x == '  ' for x in data[year][month][:7]):
                data[year][month] = data[year][month][7:]

            # this index tracks whether the given day is Saturday or Sunday. This is
            # done to style the week ends with a different background color
            index = 0
            for day in data[year][month]:
                if day == '\n':
                    html_data += '</tr><tr>'
                else:
                    # check if its a weekend to color differently
                    if ((index + 2) % 7 == 0) or ((index + 1) % 7 == 0):
                        html_data += "<td style='color: black; background: #9892B3; font-weight: bold;'>" + day + "</td>"
                    else:
                        html_data += "<td>" + day + "</td>"
                    index += 1
            html_data += '</tr>' + """
                            </tbody>
                        </table>
                    </div>
                    """
        html_data += '</div>'
    return html_data
