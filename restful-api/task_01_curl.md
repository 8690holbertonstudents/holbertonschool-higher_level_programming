<h4> 1. Consume data from an API using command line tools (curl)</h4>

<h5>1. Upon running curl --version, you should see details about your installed version of curl, including supported protocols.</h5>
 
 Learning about curl installed version with this code :
```
curl --version
```
 Returns :
```
curl 7.81.0 (x86_64-pc-linux-gnu) libcurl/7.81.0 OpenSSL/3.0.2 zlib/1.2.11 brotli/1.0.9 zstd/1.4.8 libidn2/2.3.2 libpsl/0.21.0 (+libidn2/2.3.2) libssh/0.9.6/openssl/zlib nghttp2/1.43.0 librtmp/2.3 OpenLDAP/2.5.17
Release-Date: 2022-01-05
Protocols: dict file ftp ftps gopher gophers http https imap imaps ldap ldaps mqtt pop3 pop3s rtmp rtsp scp sftp smb smbs smtp smtps telnet tftp 
Features: alt-svc AsynchDNS brotli GSS-API HSTS HTTP2 HTTPS-proxy IDN IPv6 Kerberos Largefile libz NTLM NTLM_WB PSL SPNEGO SSL TLS-SRP UnixSockets zstd
```
with all Protocols and Features supported.

<h5>2. Fetching posts from JSONPlaceholder should provide a JSON output of various posts, each having attributes like userId, id, title, and body.</h5>

With the -X flag, we can specify a method.
So with this line of code :
```
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```
The output looks like :
```
{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}
```
<h5>3. Fetching only headers should give a concise output showing status codes and headers without the actual content.</h5>

We can do that with the -I flag:
```
curl -I https://jsonplaceholder.typicode.com/posts
```
returns :
```
HTTP/2 200 
date: Wed, 29 May 2024 17:55:24 GMT
content-type: application/json; charset=utf-8
report-to: {"group":"heroku-nel","max_age":3600,"endpoints":[{"url":"https://nel.heroku.com/reports?ts=1716925149&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&s=7C7N4FlhBnL33c%2FB%2B7VDAK4GkBihcD4vjwJhXj1rsRM%3D"}]}
reporting-endpoints: heroku-nel=https://nel.heroku.com/reports?ts=1716925149&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&s=7C7N4FlhBnL33c%2FB%2B7VDAK4GkBihcD4vjwJhXj1rsRM%3D
nel: {"report_to":"heroku-nel","max_age":3600,"success_fraction":0.005,"failure_fraction":0.05,"response_headers":["Via"]}
x-powered-by: Express
x-ratelimit-limit: 1000
x-ratelimit-remaining: 999
x-ratelimit-reset: 1716925160
vary: Origin, Accept-Encoding
access-control-allow-credentials: true
cache-control: max-age=43200
pragma: no-cache
expires: -1
x-content-type-options: nosniff
etag: W/"6b80-Ybsq/K6GwwqrYkAsFxqDXGC7DoM"
via: 1.1 vegur
cf-cache-status: HIT
age: 22558
server: cloudflare
cf-ray: 88b85aed28292c87-DFW
alt-svc: h3=":443"; ma=86400
```
<br>
<h5>4. Making a POST request should yield a response from the server acknowledging the reception of the data. For JSONPlaceholder, it typically returns the created post with an id of 101 (since it doesn’t actually save the new post, but simulates the creation).</h5>

The code :
```
curl -X POST https://jsonplaceholder.typicode.com/posts
```
The output :
```
{
  "id": 101
}
```
