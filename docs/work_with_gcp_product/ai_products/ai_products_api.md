# Cloud Natural Language API

## Create an API Key
```shell
export GOOGLE_CLOUD_PROJECT=$(gcloud config get-value core/project)

gcloud iam service-accounts create my-natlang-sa \
  --display-name "my natural language service account"
  
gcloud iam service-accounts keys create ~/key.json \
  --iam-account my-natlang-sa@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com 
  
export GOOGLE_APPLICATION_CREDENTIALS="/home/USER/key.json"
```

## Make an Entity Analysis Request

```shell
gcloud ml language analyze-entities --content="Michelangelo Caravaggio, Italian painter, is known for 'The Calling of Saint Matthew'." > result.json
```

# Google Cloud Speech API
## Create an API Key
```shell
gcloud iam service-accounts create quickstart

gcloud iam service-accounts keys create key.json --iam-account quickstart@qwiklabs-gcp-02-49c8833cb196.iam.gserviceaccount.com

gcloud auth activate-service-account --key-file key.json

gcloud auth print-access-token
```

## Create your Speech API request
```shell
cat > request.json <<EOF
{
  "config": {
      "encoding":"FLAC",
      "languageCode": "en-US"
  },
  "audio": {
      "uri":"gs://cloud-samples-tests/speech/brooklyn.flac"
  }
}
EOF
```
## Call the Speech API

```shell
curl -s -X POST -H "Content-Type: application/json" --data-binary @request.json \
"https://speech.googleapis.com/v1/speech:recognize?key=${API_KEY}"

curl -s -X POST -H "Content-Type: application/json" --data-binary @request.json \
"https://speech.googleapis.com/v1/speech:recognize?key=${API_KEY}" > result.json
```

# Video Intelligence

## Set up authorization
```shell
gcloud iam service-accounts create quickstart

gcloud iam service-accounts keys create key.json --iam-account quickstart@qwiklabs-gcp-02-49c8833cb196.iam.gserviceaccount.com

gcloud auth activate-service-account --key-file key.json

gcloud auth print-access-token
```

## Make an annotate video request

```shell
cat > request.json <<EOF
{
   "inputUri":"gs://spls/gsp154/video/train.mp4",
   "features": [
       "LABEL_DETECTION"
   ]
}
EOF

curl -s -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer '$(gcloud auth print-access-token)'' \
    'https://videointelligence.googleapis.com/v1/videos:annotate' \
    -d @request.json

PROJECTS=917545686469
LOCATIONS=asia-east1
OPERATION_NAME=2557354518919161508
curl -s -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer '$(gcloud auth print-access-token)'' \
    "https://videointelligence.googleapis.com/v1/projects/${PROJECTS}/locations/${LOCATIONS}/operations/${OPERATION_NAME}"
```

