INTRODUCTION

The scouting.org website used for rechartering is an IE only site, but
only because some of the Javascript on the site doesn't work properly with
Safari or Chrome.

This proxy fixes the Javascript so that you can recharter using Chrome
(I haven't tested it with Safari).  It use proxpy and sits between
your browser and scouting.org, fixing up the Javascript as it goes
through.

TO USE
1) Download proxpy from https://code.google.com/p/proxpy/
2) mv scoutingorg.py into proxpy/plugins
3) Run "python proxpy.py -x plugins/scoutingorg.py"
4) Setup your web browser to use localhost:8080 as a proxy

