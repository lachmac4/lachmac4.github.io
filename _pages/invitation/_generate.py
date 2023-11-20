import csv
import os
with open('c:/Users/lachl/Documents/Wedding/lachmac4.github.io/_pages/invitation/_data.csv', newline='') as csvfile:
    datareader = csv.reader(csvfile, delimiter='\t', quotechar='"')
    for row in datareader:
        filestr = """---
layout: invitation-page-reception
subtitle: "{}"
permalink: "{}"
---
        """.format(row[0],row[2])
        fname = row[2].strip("/") + ".md"
        # os.remove("c:/Users/lachl/Documents/Wedding/lachmac4.github.io/_pages/invitation/" + fname)
        f = open("c:/Users/lachl/Documents/Wedding/lachmac4.github.io/_pages/invitation/" + fname, "w")
        f.write(filestr)
        f.close()
