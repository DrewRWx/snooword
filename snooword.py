#!/usr/bin/python

# SnooWord
# Written by DrewRWx .


# !!!
# These values need to be set!
USERNAME = None
SUBREDDIT = None
KEYWORDS = []
# !!!


import praw

import re

import tempfile

from subprocess import call
import os

# This is optional and not recommended, but streamlines running the script.
PASSWORD = None

# Authenticates with reddit and gets as many of the newest comments from the subreddit as possible.
r = praw.Reddit('Keyword mention checker by u/DrewRWx')
r.login(USERNAME, PASSWORD)
s = r.get_subreddit(SUBREDDIT)
comments = s.get_comments(limit=None)

# l holds each line of the report until they are written to the tempfile in one fell swoop.
l = []

# One liner to add subreddit flair text if it exists.
ifflair = lambda s: ' ('+s+')' if (s != '') else ''

# The report is peppered with Markdown and contains the newest posts in the subreddit that KEYWORDS occur in:
# _ TITLE _
# ` USER ${FLAIR} `
# PERMALINK
#
# POST BODY
#
#
for comment in comments:
	# If there is a case insensitive keyword match, include the comment.
	if any(re.search(keyword, comment.body, re.IGNORECASE) for keyword in KEYWORDS):
		l.append('_' + comment.link_title + '_  ')
		l.append('`' + comment.author.name + ifflair(comment.author_flair_text) + '`  ')
		l.append(comment.permalink + '  ')
		l.append('')
		l.append(comment.body)
		l.append('')
		l.append("---")
		l.append('')

# mad(1) needs to read from a file, so put it in a temp directory.
f = tempfile.NamedTemporaryFile(delete=False)
# Join all the strings as individual lines and avoid an ascii error.
f.write("\n".join(l).encode("utf-8"))
# Close tempfile after it is written to.
f.close()

# Run the mad(1) markdown in the submodule relative to the script's directory.
dirpath = os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir))+"/"
call([dirpath+"mad/bin/mad", f.name])

# Cleanup tempfile.
call(["rm", f.name])

