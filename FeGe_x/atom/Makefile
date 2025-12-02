include ../rspthome

../atomdens: atomdens.form element_32.a element_26.up
	stick atomdens.form >$(@)

element_32.a: data_32.a
	cp data_32.a atom.data; $(RSPTHOME)/bin/atom; mv atom.dens $(@)
	mv atom.out out_32.a; mv wavef_chars radii_32.a; rm -f j* atom.data wavef*

element_26.up: data_26.up
	cp data_26.up atom.data; $(RSPTHOME)/bin/atom; mv atom.dens $(@)
	mv atom.out out_26.up; mv wavef_chars radii_26.up; rm -f j* atom.data wavef*

