test:
	docker build . -t test-hello-world && docker run --rm -ti test-hello-world
