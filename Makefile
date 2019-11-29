TOPTARGETS := all clean test bundle build lambci

SUBDIRS := \
	examplecommon \
	entrystep \
	storestep \
	wordservice

$(TOPTARGETS): $(SUBDIRS)
$(SUBDIRS):
	@echo $@: $(MAKECMDGOALS)
	@$(MAKE) -C $@ $(MAKECMDGOALS)

.PHONY: $(TOPTARGETS) $(SUBDIRS)
