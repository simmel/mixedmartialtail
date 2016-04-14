BLUECOAT_LOGS=$(foreach INT,$(BLUECOAT_FILES),Demo_log_00$(INT).log)
BLUECOAT_FILES=1 2 3 4
PERCENTAGES=0 25 50 75 100
JSON_LOGS=$(foreach PERCENT,$(PERCENTAGES),mmt_json_$(PERCENT)p.log)

all: $(JSON_LOGS)

bluecoat_proxy_big.zip:
	curl -LO http://log-sharing.dreamhosters.com/bluecoat_proxy_big.zip

$(BLUECOAT_LOGS): bluecoat_proxy_big.zip
	unzip -n bluecoat_proxy_big.zip
	touch $@

demo_w3c.log: $(BLUECOAT_LOGS)
	time cat Demo_log_00*.log | ../tests/bluecoat_convert.pl | iconv -f latin1 -t utf8 > demo_w3c.log

mmt_json_%p.log: demo_w3c.log
	time cat demo_w3c.log | PERCENTAGE=$* logstash agent -f ../tests/to_mixed_json_format.conf > $@
