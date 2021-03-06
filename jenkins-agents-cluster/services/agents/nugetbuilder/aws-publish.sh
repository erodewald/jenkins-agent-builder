ECS_IMAGE=nuget-builder
ECS_REPO_TAG="$ECS_IMAGE:latest"
ECS_REPO="840774847457.dkr.ecr.us-east-1.amazonaws.com/$ECS_REPO_TAG"
ZONE=us-east-1

docker build -t "$ECS_IMAGE" .
docker tag "$ECS_REPO_TAG" "$ECS_REPO"

# Login to AWS ECR Repository
eval "$( aws ecr get-login --no-include-email )"

docker push "$ECS_REPO"