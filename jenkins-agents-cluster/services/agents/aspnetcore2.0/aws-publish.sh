ECS_IMAGE=aspnetcore2.0
ECS_REPO_TAG="$ECS_IMAGE:latest"
ECS_REPO="840774847457.dkr.ecr.us-east-1.amazonaws.com/$ECS_REPO_TAG"

docker build -t "$ECS_IMAGE" .
docker tag "$ECS_REPO_TAG" "$ECS_REPO"

# Install ECR login plugin so we don't need to login

# Login to AWS ECR Repository
eval "$( aws ecr get-login --no-include-email )"

docker push "$ECS_REPO"