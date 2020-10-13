# FIXME: before you push into master...
RUNTIMEDIR=F:/OpenModelica1.16.0-dev.03-64bit/include/omc/c/
#COPY_RUNTIMEFILES=$(FMI_ME_OBJS:%= && (OMCFILE=% && cp $(RUNTIMEDIR)/$$OMCFILE.c $$OMCFILE.c))

fmu:
	rm -f FeedBack.fmutmp/sources/FeedBack_init.xml
	cp -a "F:/OpenModelica1.16.0-dev.03-64bit/share/omc/runtime/c/fmi/buildproject/"* FeedBack.fmutmp/sources
	cp -a FeedBack_FMU.libs FeedBack.fmutmp/sources/

