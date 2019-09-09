.PHONY: build
build:
	hugo

.PHONY: publish
publish:
	cd public; \
	git add . ; \
	git commit -m"Release $$(date)"; \
	git push;

.PHONY: server
server:
	hugo server --bind 0.0.0.0 -D
