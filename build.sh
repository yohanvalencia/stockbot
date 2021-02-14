#!/usr/bin/env bash

DEFAULT=0

read -p "$(echo -e 'Choose an option (default [0]):\n[0] Push to Heroku and Docker Hub\n[1] Push to Heroku\n[2] Push to Docker Hub\n[3] Exit\n>')" OPTION
PROCEED=${OPTION:-$DEFAULT}
echo $PROCEED

case $PROCEED in

0)
  echo "Pushing to Heroku and Docker Hub..."
  heroku container:push web -a $HEROKU_APP_NAME
  heroku container:release web -a $HEROKU_APP_NAME
  docker image build -t $DOCKERHUB_USERNAME/$IMAGE_NAME:$VERSION .
  docker image push $DOCKERHUB_USERNAME/$IMAGE_NAME:$VERSION
  echo "Done!"
  ;;
1)
  echo "Pushing to Heroku..."
  heroku container:push web -a $HEROKU_APP_NAME
  heroku container:release web -a $HEROKU_APP_NAME
  echo "Done!"
  ;;
2)
  echo "Pushing to Docker Hub..."
  docker image build -t $DOCKERHUB_USERNAME/$IMAGE_NAME:$VERSION .
  docker image push $DOCKERHUB_USERNAME/$IMAGE_NAME:$VERSION
  echo "Done!"
  ;;
3)
  echo "Bye!"
  exit
  ;;

esac
