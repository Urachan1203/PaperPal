# PaperPal
A Slack bot introduces a new paper.

## Usage
### main
```
$ export QUERY_API_ENDPOINT=<your api endpoint>
$ export SLACK_API_KEY=<your slack api key>
$ python main.py
```
### Slack API Serv
```
$ tmux new -s apisrv

// run in the tmux session (apisrv)
$ python api_srv.py
```

## Use cron
```
QUERY_API_ENDPOINT=<yout api endpoint>
SLACK_API_KEY=<our slack api key>
1 0 * * 1-5 /path/to/python /path/to/main.py
```
