# Mixed martial tail

mmt is a warlike and bruteforce approach to tailing logs with mixed formats in them.

## TODO
* Have as few options as possible and have sane defaults.
* Plugin structure for formats so new ones can be added easily
* Follow the [UNIX philosophy](https://en.wikipedia.org/wiki/Unix_philosophy#Do_One_Thing_and_Do_It_Well) to do one thing and do it well.
  * Don't tail; `tail -F` can do that so much better.
* Support JSON
  * CSS selectors
  * JSONPath
* Offer the option to just the Syslog message part or replace the whole line.
* Add benchmarks and run them on TravisCI on every commit. Make sure we log in a structured way so we can create a graph of how slow we are.
  * Add a few log files for the test:
    * One huge
    * 100% Syslog
    * 75/25 Syslog/JSON
    * 50/50 Syslog and JSON
    * 75/25 JSON/Syslog

## Future TODO
* Support [GELF](http://docs.graylog.org/en/latest/pages/gelf.html)
* Support XML(!)
