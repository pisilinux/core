#!/bin/sh -e

CERT=/etc/openssl/certs/apache.pem
export RANDFILE=/dev/random

if [ "$1" != "--force" -a -f $CERT ]; then
  echo "$CERT exists!  Use \"$0 --force.\""
  exit 0
fi

if [ "$1" == "--force" ]; then
  shift
fi     

echo
echo creating selfsingned certificate
echo "replace it with one signed by a certification authority (CA)"
echo
echo enter your ServerName at the Common Name prompt
echo
echo If you want your certificate to expire after x days call this programm 
echo with "-days x". Default: 30 days

# use special .cnf, because with normal one no valid selfsigned
# certificate is created

openssl req $@ -config /etc/openssl/openssl.cnf \
  -new -x509 -nodes -out $CERT -keyout $CERT
  
chmod 600 $CERT

ln -sf $CERT \
  /etc/openssl/certs/`/usr/bin/openssl x509 -noout -hash < $CERT`.0
