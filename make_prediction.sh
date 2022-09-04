#!/usr/bin/env bash
PORT=5000
echo "Port: $PORT"

# POST method predict
curl -d \
         '{
            "message": [
               "go jurong point crazy available bugis n great world la e buffet cine got amore wat",
               "ok lar joking wif oni",
               "free entry wkly comp win fa cup final tkts 21st may 2005 text fa 87121 receive entry questionstd txt ratetcs apply 08452810075over18s",
               "nah think goes usf lives around though"
            ]
         }'\
     -H "Content-Type: application/json" \
     -X POST http://localhost:$PORT/predict