# Photo Gallery

Running with steps above:
  
  ### Running with

    export AWS_ACCESS_KEY_ID=<aws_access_key_id>
    export AWS_SECRET_ACCESS_KEY=<aws_access_key>

    AWS_ACCESS_KEY_ID=$(aws --profile default configure get aws_access_key_id)
    AWS_SECRET_ACCESS_KEY=$(aws --profile default configure get aws_secret_access_key)

    docker build -t photogallery .
    
    docker run -d \
    -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
    -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
    -p 8000:8000/tcp \
    photogallery


Access http://localhost:8000
