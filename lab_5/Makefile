STATES := app tests
REPO := annkravchuk/lab4-example

.PHONY: $(STATES)

$(STATES):
	@docker build -f Dockerfile.$(@) -t $(REPO):$(@) .

run:
	@docker network create --driver=bridge appnet \
	&& docker run --rm --name redis --net=appnet -d redis \
	&& docker run --rm -it --name app --net=appnet -p 5000:5000 $(REPO):app

push-hub:
	@docker push $(REPO):app
	@docker push $(REPO):tests

test-app:
	@docker run --rm -it --name test --net=appnet $(REPO):tests

del-img:
	@docker image prune -af

docker-prune:
	@@docker rm $$(docker ps -a -q) --force || true \
	&& docker container prune --force \
	&& docker volume prune --force \
	&& docker network prune --force \
	&& docker image prune --force


