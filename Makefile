.PHONY: build
build:
	hugo

.PHONY: publish
publish:
	cd public; \
	git add . ; \
	git commit -m"Release $$(date)"; \
	git push;


