TOPTARGETS := all clean test bundle build lambci

SUBDIRS := \
	examplecommon \
	wordstep \
	storestep \
	wordservice

$(TOPTARGETS): $(SUBDIRS)
$(SUBDIRS):
	@echo $@: $(MAKECMDGOALS)
	@$(MAKE) -C $@ $(MAKECMDGOALS)

.PHONY: $(TOPTARGETS) $(SUBDIRS)
