<h2 align="center">

PROXY SCRAPPER

</h2>

Proxy Scrapper that scrapes proxy and check the proxies (http only) from ~40 source. Need help to fix shit code.

# Download

- HTTP(s)
  ```bash
  # Original
  wget https://raw.githubusercontent.com/ReCaree/proxy-scrapper/master/proxy/http.txt
  # Duplicates Removed
  wget https://raw.githubusercontent.com/ReCaree/proxy-scrapper/master/proxy/http-removed.txt
  ```
- SOCKS4

  ```bash
  # Original
  wget https://raw.githubusercontent.com/ReCaree/proxy-scrapper/master/proxy/socks4.txt
  # Duplicates Removed
  wget https://raw.githubusercontent.com/ReCaree/proxy-scrapper/master/proxy/socks4-removed.txt
  ```

- SOCKS5
  ```bash
  # Original
  wget https://raw.githubusercontent.com/ReCaree/proxy-scrapper/master/proxy/socks5.txt
  # Duplicates Removed
  wget https://raw.githubusercontent.com/ReCaree/proxy-scrapper/master/proxy/socks5-removed.txt
  ```

# Setup

- Clone this repository and install requirement with:

  ```bash
  pip install -r requirements.txt
  ```

- Run the scrapper.

  ```bash
  python scrapper.py
  ```

# Todo

- Add SOCK 4/5 checker
- Better multithreading

# Contributing

Fell free to contribute. Add fixes or source.
