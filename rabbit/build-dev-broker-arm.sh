#!/bin/bash
set -euo pipefail
cp DevRabbitArmDockerfile Dockerfile
GIT_COMMIT=$(git rev-parse --short HEAD)
FIRST_DOCKER_NAME_COMPONENT="jessmillar"
SECOND_DOCKER_NAME_COMPONENT="dev-rabbit-arm"
DOCKER_IMAGE_NAME="${FIRST_DOCKER_NAME_COMPONENT}/${SECOND_DOCKER_NAME_COMPONENT}"

if [[ $(git status --untracked-files=no --porcelain) != '' ]]; then
  # uncomitted changes exist in tracked files
  ANNOTATED_GIT_COMMIT="$GIT_COMMIT-DIRTY"
  DOCKER_IMAGE_TAG="chaos__dev"
else
  # Working directory clean, modulo untracked files
  ANNOTATED_GIT_COMMIT=$GIT_COMMIT
  DOCKER_IMAGE_TAG="chaos__${GIT_COMMIT}__$(date +'%Y%m%d')"
fi
GRIDWORKS_DOCKERIMG_ID="${DOCKER_IMAGE_NAME}__${ANNOTATED_GIT_COMMIT}__$(date +'%Y%m%d')"

echo "docker image tag is ${DOCKER_IMAGE_TAG}"
echo "gridworks docker image id is ${GRIDWORKS_DOCKERIMG_ID}"
echo "docker image name is ${DOCKER_IMAGE_NAME}"

docker build  -t $DOCKER_IMAGE_NAME:$DOCKER_IMAGE_TAG --label "gridworks_docker_id=${GRIDWORKS_DOCKERIMG_ID}"  --build-arg gridworks_dockerimg_id=$GRIDWORKS_DOCKERIMG_ID .

docker tag $DOCKER_IMAGE_NAME:$DOCKER_IMAGE_TAG $DOCKER_IMAGE_NAME:latest
docker push $DOCKER_IMAGE_NAME:$DOCKER_IMAGE_TAG

rm Dockerfile
