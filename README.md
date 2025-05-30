# Build the image
```
docker build -t citrixcloud .
```

# Run the image
```
docker run -it --rm -v $(pwd):/app citrixcloud
```