# Mixed martial tail

mmt is a warlike and bruteforce approach to tailing logs with mixed formats in them.

Having structured logs in e.g. JSON is nice and makes it easy (and fast!) to
parse and index them. However this also means that logs aren't that easy to
read on the machine which creates the logs (hello Java stacktraces!).

mixedmartialtail is the answer to this problem and makes it easy to read logs
with tail even if they are structured!

## Installation

```
# Until it's up on PyPI:
$ git clone https://github.com/simmel/mixedmartialtail
$ pip install .
```

## Usage

```
$ tail -F /var/log/messages | mmt
# You can even pipe it further to less(1) or even ccze(1) or colortail(1)
$ tail -F /var/log/messages | mmt | ccze -A
```

## Design
### Main program
* [X] Load all plugins via `PluginManager.load_setuptools_entrypoints`
* [X] Read one line at the time, buffers turned off (I guess?)
* [X] Use `pm.hook.match(line=line)` to see if that line matches and then:
  * [X] Run the `pm.hook.apply(line=line)` method
* [X] Check if we're supposed to replace the whole line or just the message part.

#### Plugin
* [Registers an entry point](https://setuptools.readthedocs.io/en/latest/setuptools.html#dynamic-discovery-of-services-and-plugins)
* 1:N calls: "firstresult"
* "cat" plugin attributed "trylast"
* setuptools based entry points.

### Plugin
* `apply` method which takes a line and format options as input and transforms the line into a the format we want.
* `add_argument` method which enables the plugin to add options.

## Guidelines
* Have as few options as possible and have sane defaults.
* Plugin structure for formats so new ones can be added easily
* Follow the [UNIX philosophy](https://en.wikipedia.org/wiki/Unix_philosophy#Do_One_Thing_and_Do_It_Well) to do one thing and do it well.
  * Don't tail; `tail -F` can do that so much better.

## TODO
* [X] Add usage in README
* [X] Add option to continue even if JSON is broken.
* [X] Offer the option to just the Syslog message part or replace the whole line.
* [X] Add hostname when replacing the whole line
* [ ] Add example code for every supported log lib
* [ ] Fix date and time tests
  * [X] Wrong TZ because of DST and we're using `time.strftime('%z')`
  * [ ] In json_log_formatter there's no TZ
  * [ ] log_formatter logrus logstashV1 gets crazy
  * [ ] ms is rounded up, should it?
  * [ ] Colon or no colon. Can the test ignore if the colon is there or not?
  * [X] Negative timezone doesn't work
* [X] Add prog name and log level even when not using -i
* [X] Use datetime.isoformat() instead of strftime() for speed
* [X] When TZ is +0000 use Z instead. Maybe use datetime.isoformat()?
* [X] Format milliseconds to 3 digits
* [X] format_date on 13 should be 013
* [X] Deal with BrokenPipeError and KeyboardInterrupt
* [X] Use [tox-travis](https://pypi.python.org/pypi/tox-travis)?
* [X] Add option to not replace the TZ when it doesn't exist?
* [ ] Figure out how to use tox to run benchmarks on all Python versions
* [ ] Release 1.0.0 on PyPI
## TODO After benchmarks added
* [ ] format_date should use tz of date parsed not current date
* [ ] Add support for selecting fields via [JMESPath](https://github.com/jmespath/jmespath.py)
  * [ ] Use it ourselves for the default
  * [ ] Add an option to specify your own JMESPath
  * [ ] Detect and use previously viewed syslog format
* [ ] Add [benchmarks](https://pypi.python.org/pypi/pytest-benchmark/) and run them on TravisCI on every commit. Make sure we log in a structured way so we can create a graph of how slow we are.
  * Add a few log files for the test:
    * One huge
    * 100% Syslog
    * 75/25 Syslog/JSON
    * 50/50 Syslog and JSON
    * 75/25 JSON/Syslog
  * Use [these](http://log-sharing.dreamhosters.com/) as a baseline.
    * Convert the Apache ones to json via Logstash.
* [X] Disable buffering from the beginning
  * [ ] Enable buffering after a while based on how fast the data is flowing?
* [ ] Do the JSON parsing faster
  * [ ] insert them into a FIFO queue
  * [ ] and use a thread worker pool on that queue
* [ ] Fix bluecoat_convert on these URLs:
  * `/_vti_bin/_vti_aut/fp30reg.dll`
  * Support querystrings such as `?client=navclient-auto`
* [ ] Rewrite bluecoat_converter in Logstash instead of Perl
  * Investigate why the LS version is slower than the Perl one

## Future TODO
* Support [GELF](http://docs.graylog.org/en/latest/pages/gelf.html)
* Support XML(!)
