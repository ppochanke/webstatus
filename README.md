# webstatus
Little python project with unit tests

Run `python websocket.py` with `-u` or `--url` parameter to get status code of specified page.

Use `-f` or `--follow-redirects` to bypass 3XX (301, 302 etc.) status.

### Example:
`python websocket.py -u http://google.com` returns `Requested site status:  301`

`python websocket.py -u http://google.com -f` returns `Requested site status: 200`


## Unit tests
To run unit tests just use `python -m unittest test.py`
