<h1>Translate</h1>
<h2>Simple command line tool for croatian/english translation</h2>
<h3>Install</h3>
<p>
You will need pip tool for python to install renamer into your shell environment.<br />
Pip is included in python 3.x+<br />
Tool is compatible with python 2.7+<br />
<br />
$ git clone https://github.com/capJavert/python-translate.git python-translate<br />
$ cd python-translate <br />
$ pip install --editable .<br />
(you have to be root on linux or sudo <b>pip install --editable .</b> )<br />
<br />
After install you can use script as: <br />
<b>$ translate --word=woman</b>
</p>
<h3>Usage</h3>
<p>
Usage: translate [OPTIONS]<br />
<br />
Options:<br />
  --word TEXT  Word that you wish to translate.<br />
  --lang TEXT  Language in which word is wrote ("en" or "hr"). Default is<br />
               english language.<br />
  --help       Show this message and exit.<br />

<h3>Credits</h3>
Thanks to <a href="http://www.design-ers.net">http://www.design-ers.net</a> for such a cool and fast translation website<br />
My tool only sends request to there website i do not own a translation algorithm or word database.<br />

<h3>To do</h3>
- Add other languages<br />
