#!/usr/bin/env perl
use strict;
use warnings;
use Data::Dumper;
use POSIX 'strftime';
use Date::Parse;

while (<>) {
#65.211.15.112 - - [02/Aug/2005:07:59:48 -0400] "GET /phpBB/templates/subSilver/subSilver.css HTTP/1.1" 200 7234 "http://63.126.79.67/phpBB/install/install.php" "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.6) Gecko/20050225 Firefox/1.0.1"
#2005-04-13 18:43:38 48 192.16.170.46 200 TCP_NC_MISS 2919 551 GET https 192.16.170.42 /av-banner.html - - DEFAULT_PARENT 10.0.1.6 text/html "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.6) Gecko/20050317 Firefox/1.0.2" PROXIED none - 192.16.170.42 SG-HTTPS-Service - none -
  chomp;
  if (/^(?<date>.+?) (?<time>.+?) .+? (?<ip>.+?) (?<http_status>.+?) .+? .+? (?<bytes>.+?) (?<http_method>.+?) .+? .+? (?<url>.+?) .+? .+? .+? .+? .+? (?<useragent>(?:".+?"|-)) .*/) {
#    print Dumper \%+;
    my $date = str2time("$+{date} $+{time}");
    $date = strftime("%d/%b/%Y:%T %z", gmtime($date));
    print "$+{ip} - - [$date] \"$+{http_method} $+{url} HTTP/1.0\" $+{http_status} $+{bytes} \"-\" $+{useragent}\n";
  }
  elsif (/^#/) {}
  else {
    die $_;
  }
}
