# Mixed martial tail

mmt is a warlike and bruteforce approach to tailing logs with mixed formats in them.

## Design
### Main program
* Load all the plugins and add their "name" to an array.
* Read one line at the time, buffers turned off (I guess?)
* Loop through all of the plugins matchers on that line and if it matches:
  * Run the apply method on the line
* Check if we're supposed to replace the whole line or just the message part.

### Plugin
* `match` method which takes a line as input and see if we want to deal with this line.
* `apply` method which takes a line and format options as input and transforms the line into a the format we want.

## Guidelines
* Have as few options as possible and have sane defaults.
* Plugin structure for formats so new ones can be added easily
* Follow the [UNIX philosophy](https://en.wikipedia.org/wiki/Unix_philosophy#Do_One_Thing_and_Do_It_Well) to do one thing and do it well.
  * Don't tail; `tail -F` can do that so much better.

## TODO
* Support JSON
  * CSS selectors
  * JSONPath
* Offer the option to just the Syslog message part or replace the whole line.
* Add [benchmarks](https://pypi.python.org/pypi/pytest-benchmark/) and run them on TravisCI on every commit. Make sure we log in a structured way so we can create a graph of how slow we are.
  * Add a few log files for the test:
    * One huge
    * 100% Syslog
    * 75/25 Syslog/JSON
    * 50/50 Syslog and JSON
    * 75/25 JSON/Syslog
  * Use [these](http://log-sharing.dreamhosters.com/) as a baseline.
    * Convert the Apache ones to json via Logstash.
* Disable buffering from the beginning
  * Enable buffering after a while based on how fast the data is flowing?

## Future TODO
* Support [GELF](http://docs.graylog.org/en/latest/pages/gelf.html)
* Support XML(!)
