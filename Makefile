.PHONY: build
build:
	hugo

.PHONY: publish
publish: build
	cd public
	git add .
	git commit -m"Release $$(date)"
	git push

