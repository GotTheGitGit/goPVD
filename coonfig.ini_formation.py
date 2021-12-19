import configparser

channel_access_token = 'Cm+w+ol6MwLL8N0j4kOricthYXR69M8utl/8rJbh6JuKW3esQhDeADpCh3EcwDwRs3TiryeSselVGVo2gf880e/+N28FefuSSjh/kIef6cXbPOPzHR7LZRwm1iAMuCGsLSwQVYrcM/rjFQ/jGSy8awdB04t89/1O/w1cDnyilFU='
channel_secret = '26f54f5f7894144be2856af9eb732968'

config = configparser.ConfigParser()
config['line-bot'] = {}
config['line-bot']['channel_access_token'] = channel_access_token
config['line-bot']['channel_secret'] = channel_secret

with open('config.ini', 'w') as f:
    config.write(f)