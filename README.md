# Build the image
```
docker build -t citrixcloud .
```

# Run the image
```
docker run -it --rm -v $(pwd):/app citrixcloud
```

Odata library will download the metadata to create reflection. This data will be downloaded in the working directory. This means that the
`PYTHONPATH` variable needs to be set to the working directory.