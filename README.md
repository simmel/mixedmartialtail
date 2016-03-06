# Mixed martial tail

mmt is a warlike and bruteforce approach to tailing logs with mixed formats in them.

## TODO
* Plugin structure for formats so new ones can be added easily
* Follow the [UNIX philosophy](https://en.wikipedia.org/wiki/Unix_philosophy#Do_One_Thing_and_Do_It_Well) to do one thing and do it well.
  * Don't tail; `tail -F` can do that so much better.
* Support JSON
  * CSS selectors
  * JSONPath
* Offer the option to just the Syslog message part or replace the whole line.

## Future TODO
* Support [GELF](http://docs.graylog.org/en/latest/pages/gelf.html)
* Support XML(!)
